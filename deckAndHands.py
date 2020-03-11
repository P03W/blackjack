cardnames = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King"
}

class Card:
    def __init__(self, value, court):
        self.value = value
        self.court = court

        if self.value in cardnames.keys():
            name = cardnames[self.value]
        else:
            name = str(self.value)

        if self.value > 10:
            self.value = 10

        self.name = name + " of " + self.court

    def __repr__(self):
        return self.name

class Hand:
    def __init__(self, handTitle, handtype):
        self.title = handTitle
        self.hand = []
        self.type = handtype
        self.state = "active"

    def addCard(self, card):
        self.hand.append(card)

    def isAuto(self):
        if self.type == "auto":
            return True
        else:
            return False

    def count(self):
        aces = 0
        total = 0
        for card in self.hand:
            if card.value == 1:
                aces += 1
            else:
                total += card.value
        else:
            for ace in range(aces, 0, -1):
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
        return total


    def __repr__(self):
        if self.isAuto():
            outString = self.title + "'s hand" + "\n"
        else:
            outString = self.title + " hand" + "\n"

        for card in self.hand:
            outString += str(card) + "\n"

        outString += str(self.count()) + " total"

        return outString

__all__ = ['Hand', 'Card']