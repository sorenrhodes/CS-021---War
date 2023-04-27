# Soren and Maya's final project

import random
import time


# cards
# colors don't matter

cards = []
suits = ['hearts', 'diamonds', 'spades', 'clubs']

for i in range(2,15):
    for j in suits:
        cards.append([i,j])

random.seed(0)
random.shuffle(cards)

human_cards = cards[:26]
comp_cards = cards[26:]


# rules

print("This is War! Let me explain the rules.")
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
print("Whoever collects more cards after 10 rounds wins.")
time.sleep(3)

# ready input

ready = input("Are you ready to play the game? (y/n): ").lower()
while ready == 'n' or ready != 'y':
    input("Are you ready to play the game? (y/n): ")
if ready == 'y':
    print("Let's play!")
    

# the game
    
print(f"Your card: {human_cards[0][0]} of {human_cards[0][1]}")
print(f"My card: {comp_cards[0][0]} of {comp_cards[0][1]}")
human = []
computer = []

human.append(human_cards[0:26][0])
computer.append(comp_cards[0:26][0])

# the two variables i, e is crashing the code, but not sure why yet

for i, e in range(1,11):
    count = -1
    count += 1
    while count != 10:
        print(f"Card {count}!")
        time.sleep(3)
        print(f"Your card: {human[count]} of {human_cards[0][count + 1]}")
        time.sleep(3)
        print(f"My card: {computer[count]} of {comp_cards[0][count + 1]}")
    if i in human > e in computer:
        human.pop(i)
        human.append(i)
        human.append(e)
        computer.pop(e)
    elif e in computer > i in human:
        computer.pop(e)
        computer.append(e)
        computer.append(i)
        human.pop(i)
    elif e in computer == i in human:
        if computer[4] > human[4]:         # need to print the fourth card instead of the first card, since first three are face down
            computer.pop(computer[1:4])
            computer.append(computer[1:4])
            computer.append(human[1:4])
            human.pop(human[1:4])
        elif human[4] > computer[4]:
            human.pop(human[1:4])
            human.append(human[1:4])
            human.append(computer[1:4])
            computer.pop(computer[1:4])
    if len(human) > len(computer):
        print("Game over! You win!")
    if len(computer) > len(human):
        print("Game over! I win!")
