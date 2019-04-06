class DataObject(object):


    def __init__(self):
        self.subreddits = list()
    

    def add_subreddit(self, subreddit):
        self.subreddits.append(subreddit)
