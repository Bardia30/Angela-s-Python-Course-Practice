#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Guessing Game
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo='''
 _____ _   _ _____ _____ _____ _____ _   _ _____   _____  ___ ___  ________
|  __ \ | | |  ___/  ___/  ___|_   _| \ | |  __ \ |  __ \/ _ \|  \/  |  ___|
| |  \/ | | | |__ \ `--.\ `--.  | | |  \| | |  \/ | |  \/ /_\ \ .  . | |__
| | __| | | |  __| `--. \`--. \ | | | . ` | | __  | | __|  _  | |\/| |  __|
| |_\ \ |_| | |___/\__/ /\__/ /_| |_| |\  | |_\ \ | |_\ \ | | | |  | | |___
 \____/\___/\____/\____/\____/ \___/\_| \_/\____/  \____|_| |_|_|  |_|____/
'''
print(logo)
print("welcome to the Number Guessing Game! ")

answer = random.randint(0,100)

attempts = 0
guess=0
def easy():
    global attempts
    attempts = 10

def hard():
    global attempts
    attempts = 5

def user_guess():
    global guess
    guess = int(input("Guess a number: "))
    return guess

def play_game():
    global guess
    global attempts
    user_guess()
    attempts -= 1

    while guess != answer and attempts != 0:

        if guess > answer:
            attempts -= 1
            print("Too high. Guess again. You have",attempts+1," attempts reamining")
            user_guess()
        elif guess < answer:
            attempts -= 1
            print("Too low. Guess again. You have",attempts+1," attempts reamining")
            user_guess()

        if guess == answer:
            print("That is correct you have won!")

        if attempts == 0 and guess!=answer:
            game_lost=True
            print("You have lost")


player_diff = input("What difficulty would you like? Enter 'easy' or 'hard': ").lower()

if player_diff == "easy":
    easy()
    print("You have",attempts," attempts reamining")
else:
    hard()
    print("You have",attempts," attempts reamining")
#print("pst the answer is:",answer)

play_game()
