from data_object import DataObject
from subreddit import Subreddit
import praw
import json
import time


class Crawler:


    def __init__(self):
        self.reddit = praw.Reddit('crawler')
        self.data_object = DataObject()
    

    def read_list(self):
        with open('res/subreddits-mini', 'r') as f:
            for name in f:
                subreddit_model = self.reddit.subreddit(name.rstrip())
                self.crawl(subreddit_model)
    

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
                print(f'{subreddit_model.display_name} -> OK')
                break

        self.define_subreddit(subreddit_model, moderators, recent_submissions, recent_comments)
    

    def define_subreddit(self, subreddit_model, moderators, recent_submissions, recent_comments):
        subreddit = Subreddit(
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
        with open("data/subreddit-data", "w") as f:
            f.write(json.dumps(self.data_object, default=lambda o: o.__dict__, indent=4))
