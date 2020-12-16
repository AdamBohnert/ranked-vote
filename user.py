# Contains user information and queue of ranked choices

class User:
    def __init__(self):
        # TODO: Add unique identifier from database
        self.rankings = None

        # TODO: Store user in database

    # sort rankings
    def vote(self, choices):
        self.rankings = {k: v for k, v in sorted(
            choices.items(), key=lambda item: item[1])}

    # remove choice
    def remove(self, key):
        return self.rankings.pop(key, None)
