# Currently just for testing

from poll import Poll, RankedPoll
from user import User

choices = ["Adam", "Katie", "Mom"]

adam = User()
adam.vote({"Adam":1, "Katie":0, "Mom":0})

katie = User()
katie.vote({"Adam":0, "Katie":2, "Mom":0})

voters = [adam, katie]

p = Poll(choices, title="Friends")

print("winner", p.calc_winner(voters))
