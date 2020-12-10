# Currently just for testing

from poll import Poll, RankedPoll
from user import User

choices = ["Adam", "Katie", "Mom", "Dad"]

adam = User()
adam.vote({"Adam":2, "Katie":3, "Mom":1, "Dad":4})

katie = User()
katie.vote({"Adam":1, "Katie":3, "Mom":4, "Dad":2})

dad = User()
dad.vote({"Adam":4, "Katie":1, "Mom":2, "Dad":3})

voters = [adam, katie, dad]

p = RankedPoll(choices, title="Family")

print("winner", p.calc_winner(voters))
