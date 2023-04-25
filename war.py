# Soren and Maya's final project

import random
import time


# cards
# colors don't matter

cards = []
suits = ['hearts', 'diamonds', 'spades', 'clubs']

for i in range(1,14):
    for j in range(0,4):
        cards.append([i,j])

random.seed(0)
random.shuffle(cards)

human_cards = cards[:26]
comp_cards = cards[26:]

# rules

print("This is War! Let me explain the rules.")
print("I (the computer) will receive 26 cards, and you (the human) will receive 26 cards as well.")
print("We will each turn up our top cards at the same time, and whoever has the higher card") 
print("will take both cards and put them at the bottom of their deck.")
print("If the cards have the same value, it is war! We will each put three cards facedown and one faceup,")
print("and the person whose faceup card is higher will take all 8 cards.")
print("Whoever collects more cards after 10 rounds wins.")

# ready input

ready = input("Are you ready to play the game? (y/n): ").lower()
while ready == 'n' or ready != 'y':
    input("Are you ready to play the game? (y/n): ")
if ready == 'y':
    print("Let's play!")
    

# the game

def war(human, computer):
    human = []
    computer = []
    for i in range(1,11):
