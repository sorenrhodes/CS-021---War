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

print("This is the Game of War! Let me explain the rules.")
time.sleep(3)
print("I (the computer) will receive 26 cards, and you (the human) will receive 26 cards as well.")
time.sleep(3)
print("We will each turn up our top cards at the same time, and whoever has the higher card") 
time.sleep(3)
print("will take both cards and put them at the bottom of their deck.")
time.sleep(3)
print("If the cards have the same value, it is war! We will each put three cards facedown and one faceup,")
time.sleep(3)
print("and the person whose faceup card is higher will take all 8 cards.")
time.sleep(3)
print("If the cards have the same value again, the round is a tie!")
time.sleep(3)
print("Whoever collects more cards after 10 rounds wins.")
time.sleep(3)

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
