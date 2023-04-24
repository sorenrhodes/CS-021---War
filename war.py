# Soren and Maya's final project

import random
import time


# cards
# colors don't matter

values = list(range(2,15))
suits = ["clubs", "hearts", "diamonds", "spades"]
face_cards = {
    11: 'Jack',
    12: 'Queen',
    13: 'King',
    14: 'Ace'
}

# random.shuffle(cards)

# rules

print("This is War! Let me explain the rules.")
print("I (the computer) will receive 26 cards, and you (the human) will receive 26 cards as well.")
print("We will each turn up our top cards at the same time, and whoever has the higher card") 
print("will take both cards and put them at the bottom of their deck.")
print("If the cards have the same value, it is war! We will each put three cards facedown and one faceup,")
print("and the person whose faceup card is higher will take all 8 cards.")
print("Whoever collects all of the cards wins.")

# ready input

ready = input("Are you ready to play the game? (y/n): ").lower()
while ready == 'n' or ready != 'y':
    input("Are you ready to play the game? (y/n): ")
if ready == 'y':
    print("Let's play!")
    
# dealt cards
# random.sample makes sure the same card cannot be chosen twice

humancards = []
# humancards.append([random.sample(cards,26)])

computercards = []
# computercards.append([random.sample(cards,26)])

# the game


first_human = {random.choice(humancards)}
first_comp = {random.choice(computercards)}
first_cards = (f"Your card: {first_human} My card: {first_comp})")

