
import random

####################### Card Class #################
class Card:
    def __init__(self, value): #suit
        self.value = value
#    self.suit = []

####################### Deck Class #################
class Deck:
    def __init__(self):
        self.cards = []
        for value in range(1, 5):
            for cardamount in range(1, 11):
                self.cards.append(Card(cardamount))
            for facecard in facecards:
                self.cards.append(Card(facecard))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __str__(self):
        for card in self.cards:
            print(card.value)
        return ""

####################### Player Class #################
class Player:
    def __init__(self):
        self.hand = []

    def addcard(self, card):
        self.hand.append(card)

    def handfromdeck(self, deck):
        self.addcard(deck.draw())
        self.addcard(deck.draw())

    def hand_value(self):
        value = 0
        for card in self.hand:
            value += card.value
        return value

    def __gt__(self, other):
        return self.hand_value() > other.hand_value()

    def __eq__(self, other):
        return self.hand_value() == other.hand_value()

################## Variables ########################
A = 11  #or 1 if hand_value() > 21
K = 10
Q = 10
J = 10
facecards = [K , Q , J, A]

##########################DEBUG####################################
deck = Deck()
print(deck)

################## Game ##########################
while True:
    input()
    player_1 = Player()
    player_1.handfromdeck(deck)
    print(f"Player One: {player_1.hand_value()}")
    input("Would you like to hit? Y/N ")

    input()

    player_2 = Player()
    player_2.handfromdeck(deck)
    print(f"Player Two: {player_2.hand_value()}")
    input("Would you like to hit? Y/N ")
