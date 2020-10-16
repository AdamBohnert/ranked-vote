# Contains user information and queue of ranked choices

from collections import deque


class User:
    def __init__(self, id):
        self.id = id
        self.rankings = None

    # sort rankings
    def rank(self, choices):
        self.rankings = {k: v for k, v in sorted(
            choices.items(), key=lambda item: item[1])}

    def to_queue(self):
        return deque(self.rankings)
