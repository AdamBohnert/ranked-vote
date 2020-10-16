#! python3
# ranked_vote.py contains poll functionality


class Poll:
    def __init__(self, choices, title="Untitled Poll", user_level=0):
        self.choices = choices
        self.title = title
        self.expires = True if user_level <= 1 else False
        # TODO: Add expiration date by user level and as an option at creation

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

    # Total first-place choices
    def calc_ranked_winner(self):
        choices_copy = self.choices.copy()
        top_vote = list(self.calc_winner().items())
        num_votes = sum(self.choices.values())

        # If the top choice has 51% or more of total votes, it wins
        while top_vote[0][1] / num_votes <= 0.51:
            # Otherwise drop the choice with lowest votes
            for k, _ in self.calc_loser().items():
                # TODO: Get these users' next best choices - needs stored by
                # user
                choices_copy.pop(k)
            # TODO: Add their next choice to be compared
            break
        return top_vote

    # Finds lowest number of votes
    def calc_loser(self):
        low_val = min(self.choices.items(), key=lambda x: x[1])

        min_keys = {}
        for k, v in self.choices.items():
            if v == low_val[1]:
                min_keys.update({k: v})

        return min_keys
