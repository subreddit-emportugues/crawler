class Subreddit(object):


    def __init__(self, id, name, icon, description, members, age, nsfw, moderators, recent_submissions, recent_comments):
        self.id = id
        self.name = name
        self.icon = icon
        self.description = description
        self.members = members
        self.age = age
        self.nsfw = nsfw
        self.moderators = moderators
        self.recent_submissions = recent_submissions
        self.recent_comments = recent_comments
        