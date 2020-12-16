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
    def __init__(self, choices, title):
        super().__init__(choices, title=title)
        self.num_chices = len(self.choices.keys())

    # Total first-place choices
    def calc_winner(self, voters):
        round = 1
        pct = 0.0
        eliminated = []

        while pct < 0.51:  # No winner
            if round == 1:
                for voter in voters:
                    for k, rank in voter.rankings.items():
                        if k in self.choices and rank == round:
                            self.choices[k] += 1

            # recalculate win percentage
            s = sum(self.choices.values())
            for k, v in self.choices.items():
                pct = v * 100.0 / s
                print(k, pct, "%")

            # drop loser
            losers = self.calc_loser()
            for loser in losers:
                self.choices.pop(loser)
                eliminated.append(loser)
                print(loser, "removed.")

            # remove preferential votes for loser
            # add loser's next best choice
            for voter in voters:
                for k, rank in voter.rankings.items():
                    if rank == round and k in eliminated and k in self.choices:
                        self.choices[k] -= 1
                    if rank == round + 1 and k not in eliminated:
                        self.choices[k] += 1

            round += 1

        winner = max(self.choices.items(), key=lambda x: x[1])
        print(winner, "won in", round, "rounds.")

        return winner

    # Finds lowest number of votes
    def calc_loser(self):
        low_val = min(self.choices.items(), key=lambda x: x[1])

        min_keys = {}
        for k, v in self.choices.items():
            if v == low_val[1]:
                min_keys.update({k: v})

        return min_keys
