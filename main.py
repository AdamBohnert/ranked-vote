# Currently just for testing

from ranked_vote import RankedPoll
from user import User


data = {"Adam":30, "Katie":12, "Dustin":11}


u = User(1)
u.rank(data)

for option in u.rankings:
    print(option)


p = RankedPoll(u.rankings, title="Friends")

print(p.calc_winner())
print(p.calc_ranked_winner())
print(p.calc_loser())