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

human.append(human_cards[0][0])
human.append(human_cards[1][0])
human.append(human_cards[2][0])
human.append(human_cards[3][0])
human.append(human_cards[4][0])
human.append(human_cards[5][0])
human.append(human_cards[6][0])
human.append(human_cards[7][0])
human.append(human_cards[8][0])
human.append(human_cards[9][0])
human.append(human_cards[10][0])
human.append(human_cards[11][0])
human.append(human_cards[12][0])
human.append(human_cards[13][0])
human.append(human_cards[14][0])
human.append(human_cards[15][0])
human.append(human_cards[16][0])
human.append(human_cards[17][0])
human.append(human_cards[18][0])
human.append(human_cards[19][0])
human.append(human_cards[20][0])
human.append(human_cards[21][0])
human.append(human_cards[22][0])
human.append(human_cards[23][0])
human.append(human_cards[24][0])
human.append(human_cards[25][0])
human.append(human_cards[26][0])


computer.append(comp_cards[0][0])
computer.append(comp_cards[1][0])
computer.append(comp_cards[2][0])
computer.append(comp_cards[3][0])
computer.append(comp_cards[4][0])
computer.append(comp_cards[5][0])
computer.append(comp_cards[6][0])
computer.append(comp_cards[7][0])
computer.append(comp_cards[8][0])
computer.append(comp_cards[9][0])
computer.append(comp_cards[10][0])
computer.append(comp_cards[11][0])
computer.append(comp_cards[12][0])
computer.append(comp_cards[13][0])
computer.append(comp_cards[14][0])
computer.append(comp_cards[15][0])
computer.append(comp_cards[16][0])
computer.append(comp_cards[17][0])
computer.append(comp_cards[18][0])
computer.append(comp_cards[19][0])
computer.append(comp_cards[20][0])
computer.append(comp_cards[21][0])
computer.append(comp_cards[22][0])
computer.append(comp_cards[23][0])
computer.append(comp_cards[24][0])
computer.append(comp_cards[25][0])
computer.append(comp_cards[26][0])

for i, e in range(1,11):
    if i in human > e in computer:
        human.pop(i)
        human.append(i)
        human.append(e)
    elif e in computer > i in human:
        computer.pop(e)
        computer.append(e)
        computer.append(i)
    elif e in computer == i in human:
        if computer[4] > human[4]:
            computer.pop(1)
            computer.pop(2)
            computer.pop(3)
            computer.pop(4)
        # need to figure out how to write a range of indices
