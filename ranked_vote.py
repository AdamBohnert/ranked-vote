# !python3

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
    def calc_ranked_winner(self):
        # Total first-place choices
        choices_copy = self.choices.copy()
        top_vote = list(self.calc_winner().items())
        num_votes = sum(self.choices.values())
        
        # If the top choice has 51% or more of total votes, it wins
        while top_vote[0][1] / num_votes <= 0.51:
            # Otherwise drop the choice with lowest votes
            for k, _ in self.calc_loser().items():
                # TODO: Get these users' next best choices - needs stored by user
                choices_copy.pop(k)
            # TODO: Add their next choice to the buckets to be compared 
            break
        return top_vote

    def calc_loser(self):
        low_val = min(self.choices.items(), key=lambda x: x[1])
        
        min_keys = {}
        for k, v in self.choices.items():
            if v == low_val[1]:
                min_keys.update({k: v})
        
        return min_keys


# testing
p = RankedPoll({"Adam":30, "Katie":12, "Dustin":11}, title="Friends")

print(p.calc_winner())
print(p.calc_ranked_winner())
print(p.calc_loser())