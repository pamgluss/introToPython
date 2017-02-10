class Card:
    from random import randint
    counter = 0
    cardCatch = []

    def __init__(self):
        self.rank = getRank()
        self.suit = getSuit()
        self.bjValue = bjValue()
        Card.counter += 1

    def getSuit:
        suitSel = randint(0,3)
        suitList = ["Hearts", "Spades", "Clubs", "Diamonds"]
        suit = suitList[suitSel]
        return suit

    def getRank:
        rankSel = randint(1, 13)
        return rankSel

    def bjValue:
        bjSel = {1:[1,11], 2:2 ,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:10}
        return bjSel[self.rank]
