# Soren and Maya's final project

import random
import time


# cards
# colors don't matter

cards = []
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

for i in range(2,15):
    for j in suits:
        cards.append([i,j])

# random.seed(0)
random.shuffle(cards)

human_cards = cards[:26]
comp_cards = cards[26:]

# rules

print("This is War! Let me explain the rules.")
time.sleep(2.5)
print("I (the computer) will receive 26 cards, and you (the human) will receive 26 cards as well.")
time.sleep(2.5)
print("We will each turn up our top cards at the same time, and whoever has the higher card") 
time.sleep(2.5)
print("will take both cards and put them at the bottom of their deck.")
time.sleep(2.5)
print("If the cards have the same value, it is war! We will each put three cards facedown and one faceup,")
time.sleep(2.5)
print("and the person whose faceup card is higher will take all 14 cards.")
time.sleep(2.5)
print("Whoever collects more cards after 10 rounds wins.")

# ready input

ready = input("Are you ready to play the game? (y/n): ").lower()
while ready == 'n' or ready != 'y':
    input("Are you ready to play the game? (y/n): ")
if ready == 'y':
    print("Let's play!")
    

# the game
    
human = []
computer = []

human_won = []
comp_won = []

for i in range(0,26):
    human.append(human_cards[i][0])
    computer.append(comp_cards[i][0])


i = 0
count = 0
while count < 10:
    print(f"Card {i+1}!")
    time.sleep(2)
    print(f"Your card: {human[i]} of {human_cards[i][1]}")
    time.sleep(2)
    print(f"My card: {computer[i]} of {comp_cards[i][1]}")
    time.sleep(2)
    if human[i] > computer[i]:
        human_won.append(human[i])
        human_won.append(computer[i])
        print("Your card is higher! You win this round!")
        time.sleep(2)
    elif computer[i] > human[i]:
        comp_won.append(human[i])
        comp_won.append(computer[i])
        print("My card is higher! I win this round!")
        time.sleep(2)
    elif computer[i] == human[i]:
        print("Our cards are equal!")
        print(f"Tie breaker cards! My card: {computer[i+4]} Your card: {human[i+4]}")
        if computer[i+4] > human[i+4]:         
            comp_won.append(computer[i+4])
            comp_won.append(human[i+4])
            i += 3
            print("My card is higher! I win this round!")
            time.sleep(2)
        elif human[i+4] > computer[i+4]:
            human_won.append(human[i:i+4])
            human_won.append(computer[i:i+4])
            i += 3
            print("Your card is higher! You win this round!")
            time.sleep(2)
    i += 1
    count += 1
if len(human_won) > len(comp_won):
    print(f"Game over! You win! You won {len(human_won)} cards and I won {len(comp_won)} cards.")
if len(comp_won) > len(human_won):
    print(f"Game over! I win! You won {len(human_won)} cards and I won {len(comp_won)} cards.")
