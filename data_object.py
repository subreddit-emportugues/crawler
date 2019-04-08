import datetime


class DataObject:


    def __init__(self):
        self.subreddits = list()
        self.date = str(datetime.datetime.now())
        self.per_page = 15
        self.current_page = 1
    

    def add_subreddit(self, subreddit):
        self.subreddits.append(subreddit)


    def get_length(self):
        return len(self.subreddits)
