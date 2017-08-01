def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    sameHands = yourLeft == friendsLeft and yourRight == friendsRight
    differentHands = yourLeft == friendsRight and yourRight == friendsLeft
    return sameHands or differentHands
