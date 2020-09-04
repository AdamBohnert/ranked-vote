# !python3

import datetime

class Poll:
    def __init__(self, choices, title="Untitled Poll", user_level=0):
        self.choices = choices
        self.title = title
        self.expires = True if user_level <= 1 else False
        #self.expireDate = datetime.datetime.now() + datetime.timedelta(days=7.0)