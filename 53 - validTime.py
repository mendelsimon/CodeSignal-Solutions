def validTime(time):
    groups = time.split(":")
    if len(groups) != 2:
        return False
    if not (groups[0].isdigit() and groups[1].isdigit()):
        return False
    if int(groups[0]) > 23 or int(groups[1]) > 59:
        return False
    return True
