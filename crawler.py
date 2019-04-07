from __future__ import with_statement
from __future__ import absolute_import
from data_object import DataObject
from subreddit import Subreddit
from prawcore import exceptions
import praw
import json
import time
from io import open


class Crawler(object):


    def __init__(self):
        self.reddit = praw.Reddit('crawler')
        self.data_object = DataObject()
    

    def read_list(self):
        with open('res/subreddits', 'r') as f:
            for name in f:
                s_name = name.rstrip()
                try:
                    subreddit_model = self.reddit.subreddit(s_name)
                    self.crawl(subreddit_model)
                except exceptions.Forbidden, err:
                    print '{} is private'.format(s_name)
                    self.append_subreddit('private', s_name)
                except exceptions.NotFound, err:
                    print '{} does not exist'.format(s_name)
                    self.append_subreddit('unavailable', s_name)
    

    def crawl(self, subreddit_model):
        moderators = list()

        for moderator in subreddit_model.moderator():
            moderators.append(moderator.name)

        recent_submissions = 0
        recent_comments = 0

        for submission in subreddit_model.new(limit=None):
            if submission.created > time.time() - (24*60*60):
                recent_submissions += 1
                recent_comments += len(submission.comments.list())
            else:
                print '{} -> OK'.format(subreddit_model.display_name)
                break

        self.define_subreddit(subreddit_model, moderators, recent_submissions, recent_comments)
    

    def define_subreddit(self, subreddit_model, moderators, recent_submissions, recent_comments):
        subreddit = Subreddit(
            self.data_object.get_length(),
            subreddit_model.display_name_prefixed,
            subreddit_model.community_icon,
            subreddit_model.public_description,
            subreddit_model.subscribers,
            subreddit_model.created,
            subreddit_model.over18,
            moderators,
            recent_submissions,
            recent_comments
        )

        self.data_object.add_subreddit(subreddit)


    def write_object(self):
        with open('../data/subreddits.json', 'w') as f:
            f.write(json.dumps(self.data_object, default=lambda o: o.__dict__, indent=4).decode("UTF-8"))
    

    def append_subreddit(self, file, subreddit):
        with open('data/{}.txt'.format(file), 'a') as f:
            f.write('{}\n'.format(subreddit).decode("UTF-8"))
