# python3
# contains poll functionality


class Poll:
    def __init__(self, choices, title="Untitled Poll"):
        self.choices = {}
        for choice in choices:
            self.choices[choice] = 0

        self.title = str(title)
        # TODO: Add expiration date by user level and as an option at creation


    # Find maximum votes
    def calc_winner(self, voters):
        for voter in voters:
            for k, v in voter.rankings.items():
                if k in self.choices:
                    self.choices[k] += v
        return max(self.choices.items(), key=lambda x: x[1])

    # Store poll
    def save(self):
        pass

    # Remove poll
    def delete(self):
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
