def electionsWinners(votes, k):
    winners = 0
    current_winner = max(votes)
    for candidate in votes:
        if k > 0 and candidate + k > current_winner:
            winners += 1
        if k == 0 and candidate == current_winner and votes.count(candidate) == 1:
            winners += 1
    return winners
