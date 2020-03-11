import sys
import time
import random

from deckAndHands import *

deck = []

dealer = Hand("Dealer", "auto")
user = Hand("Your", "manual")
bot1 = Hand("Bot1", "auto")
bot2 = Hand("Bot2", "auto")
bot3 = Hand("Bot3", "auto")

hands = [
    dealer,
    user,
    bot1,
    bot2,
    bot3
]

# Make a deck with every card
for value in range(1, 14):
    for suit in ['Clubs', 'Hearts', 'Spades', 'Diamonds']:
        deck.append(Card(value, suit))

# Might be excessive? Dont know how well .shuffle() works
random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)

def hit(hand):
    hand.addCard(deck.pop())
    score = hand.count()
    if score > 21:
        time.sleep(0.3)
        print("Broke!")
        hand.state = "done"

def stand(hand):
    hand.state = "done"

for hand in hands:
    hit(hand)
    hit(hand)

while True:

    stop = True
    for hand in hands:
        if hand.state != "done":
            stop = False
    if stop:
        break

    for hand in hands:
        if hand.state != "done":
            if hand.isAuto():
                print(hand.title + "'s turn")
                time.sleep(1)
                if random.randint(0, 2) != 0:
                    print(hand.title + " hits.")
                    hit(hand)
                else:
                    stand(hand)
                    print(hand.title + " stands.")
            else:
                print(hand)
                while True:
                    decide = input("[h]it or [s]tand? ")
                    if decide in ['h', 'H', 's', 'S']:
                        break
                    else:
                        print("Invalid input")
                if decide in ['h', 'H']:
                    hit(hand)
                else:
                    stand(hand)
            print("--" * 5)
        time.sleep(0.6)
        

tophand = {"value": 0, "hand": None}
for hand in hands:
    value = hand.count()
    if value > tophand['value'] and value <= 21:
        tophand['value'] = value
        tophand['hand'] = hand

input("The winner was " + tophand['hand'].title + " with a value of " + str(tophand['value']))
print(tophand['hand'])
