def tennisSet(score1, score2):
    if max(score1, score2) == 6 and min(score1, score2) < 5:
        return True
    if 5 <= min(score1, score2) <= 6 and max(score1, score2) == 7:
        return True
    return False
