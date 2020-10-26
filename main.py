# Currently just for testing

from ranked_vote import RankedPoll
from user import User


data = {"Adam": 30, "Katie": 12, "Dustin": 11}


u = User(1)
u.rank(data)

u2 = User(2)
u2.rank({"Dustin": 30, "Adam": 11, "Katie": 5})

options = [u.rankings, u2.rankings]
for option in options:
    print(option)


p = RankedPoll(options, title="Friends") # TODO: Poll should hold possible options 
#instead of take input to be calculated

print(p.calc_winner())
print(p.calc_ranked_winner())
print(p.calc_loser())
