# Ranked Vote

## Goals:
- [ ] Implement ranked voting
- [ ] Store poll, accessible via unique url probably
- [ ] Allow voting for a selected period of time
- [ ] Remove poll from storage after awhile
- [ ] Options for duration to keep results?


### Ideas
- Build out website (possibly with normal polls as well)
- App for mobile devices
- Ads?
- Accounts?
    - What does an account do for the user?
    - Make it easy to share a poll?
    - Enforce one vote per anonymous voter


## How does it work?
One user creates a poll with some number of unique options. They share the poll with other users.
Voting users number the options with their top preference as (1), the next is (2), and so on. UI should assist with this for convenience.
When voting duration is up we total the (1) responses. If this number is 51% or greater of the number of votes cast, (1) is the winner. Otherwise, remove the choice with the lowest total from this round and add those voter's (2) choice to the totals. Repeat for each least popular option until a majority is found.

[Video demonstration](https://www.youtube.com/watch?v=oHRPMJmzBBw)

### Licence
Copyright 2020 Adam Bohnert
