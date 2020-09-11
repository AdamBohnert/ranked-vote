# !python3
# Copyright 2020 Adam Bohnert

import datetime

class Poll:
    def __init__(self, choices, title="Untitled Poll", user_level=0):
        self.choices = choices
        self.title = title
        self.expires = True if user_level <= 1 else False
        #self.expire_date = datetime.datetime.now() + datetime.timedelta(days=7.0)

    # Find maximum votes
    def calc_winner(self):
        high_val = max(self.choices.items(), key=lambda x: x[1])
        
        max_keys = {}
        for k, v in self.choices.items():
            if v == high_val[1]:
                max_keys.update({k: v})
        
        return max_keys
        
    # Store poll
    def save_poll(self):
        pass

    # Remove poll
    def del_poll(self):
        pass

    def __str__(self):
        return f"{self.title}: {[k for k in self.choices.keys()]}"


class RankedPoll(Poll):
    def calc_winner(self):
        pass


# testing
p = RankedPoll({"Adam":11, "Katie":25, "Dustin":11}, title="Friends")

print(p.calc_winner())
print(p)
