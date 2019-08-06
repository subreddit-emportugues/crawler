import datetime


class DataObject:


    def __init__(self):
        self.subreddits = list()
        self.date = str(datetime.datetime.now())
    

    def add_subreddit(self, subreddit):
        self.subreddits.append(subreddit)


    def get_length(self):
        return len(self.subreddits)
