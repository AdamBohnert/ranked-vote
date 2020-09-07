# !python3

import datetime

class Poll:
    def __init__(self, choices, title="Untitled Poll", user_level=0):
        self.choices = choices
        self.title = title
        self.expires = True if user_level <= 1 else False
        #self.expireDate = datetime.datetime.now() + datetime.timedelta(days=7.0)

    # Find maximum votes
    def calc_winner(self):
        high_val = max(self.choices.items(), key=lambda x: x[1])
        
        max_keys = {}
        for k, v in self.choices.items():
            if v == high_val[1]:
                max_keys.update({k: v})
        
        return max_keys
        


class RankedPoll(Poll):
    def calc_winner(self):
        pass


# testing
p = Poll({"Adam":11, "Katie":25, "Dustin":11})

print(p.calc_winner())