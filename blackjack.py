
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
            for facevalues in facecardvalue:
                self.cards.append(Card(facevalues))
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
facecards = {"K":10, "Q":10, "J":10, "A":11}
facecardvalue = facecards.values()


##########################DEBUG####################################
deck = Deck()
#print(f"{deck}")

################## Game ##########################
while True:
######################PLAYER 1 RULES##################
    player_1 = Player()
    player_1.handfromdeck(deck)
    print(f"Player One: {player_1.hand_value()}")    # Print the List to see cards #
    hit = input("Would you like to hit? Y/N ")
    if hit == "y":
        player_1.addcard(deck.draw())
        print(f"Player One New Total: {player_1.hand_value()}")
    hit2 = input("Would you like to hit? Y/N ")
    if hit2 == "y":
        player_1.addcard(deck.draw())
        print(f"Player One New Total: {player_1.hand_value()}")
    input()

######################PLAYER 1 RULES##################
    player_2 = Player()
    player_2.handfromdeck(deck)
    print(f"Player Two: {player_2.hand_value()}")   # Print the List to see cards #
    hit = input("Would you like to hit? Y/N ")
    if hit == "y":
        player_2.addcard(deck.draw())
        print(f"Player Two New Total: {player_2.hand_value()}")
    hit2 = input("Would you like to hit? Y/N ")
    if hit2 == "y":
        player_2.addcard(deck.draw())
        print(f"Player Two New Total: {player_2.hand_value()}")

    input()
