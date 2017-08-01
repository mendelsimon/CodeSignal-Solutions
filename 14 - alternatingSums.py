def alternatingSums(a):
    team1 = sum(a[0::2])
    team2 = sum(a[1::2])
    return [team1, team2]