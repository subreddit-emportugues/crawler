from data_object import DataObject
from io import open
from subreddit import Subreddit
from prawcore import exceptions
import json
import praw
import time



class Crawler(object):


    def __init__(self):
        self.reddit = praw.Reddit('crawler')
        self.data_object = DataObject()
    

    def read_list(self):
            for name in reversed(open('../data/subreddits.txt').readlines()):
                s_name = name.rstrip()
                try:
                    subreddit_model = self.reddit.subreddit(s_name)
                    self.crawl(subreddit_model)
                except exceptions.Forbidden as err:
                    print('{s_name} is private')
                    with open('../data/private.txt', 'a') as f:
                        f.write(s_name + '\n')
                except exceptions.NotFound as err:
                    print('{s_name} does not exist')
                    with open('../data/unavailable.txt', 'a') as f:
                        f.write(s_name + '\n')
    

    def crawl(self, subreddit_model):
        moderators = list()

        for moderator in subreddit_model.moderator():
            moderators.append(moderator.name)

        recent_submissions = 0
        recent_comments = 0

        for submission in subreddit_model.new(limit=None):
            if submission.created > time.time() - (24*60*60):
                recent_submissions += 1
                recent_comments += submission.num_comments
            else:
                print('{} -> OK'.format(subreddit_model.display_name))
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
            f.write(json.dumps(self.data_object, default=lambda o: o.__dict__, indent=4))
