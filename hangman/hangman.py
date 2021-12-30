import random
import words
import os
import platform
from man import man
win = False
lost = False
difficulty_chosen = False
guessed_list = []
wrong = 10
secret_list = []
point = 0
accepted_characters = "abcdefghijklmnopqrstuvwxyz"

def clear_console():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        os.system('cls')

def pick_word(difficulty):

    if difficulty == '1': secret = random.choice(words.easy)
    elif difficulty == '2': secret = random.choice(words.medium)
    elif difficulty == '3': secret = random.choice(words.hard)
    return secret

clear_console()
while not difficulty_chosen:
    difficulty = input("Press 1 for easy\nPress 2 for medium\nPress 3 for hard\n")
    if difficulty == '1' or difficulty == '2' or difficulty == '3':
        secret = pick_word(difficulty)
        difficulty_chosen = True
    else:
        clear_console()
        print("Enter a valid option\n")

for i in range(len(secret)):
    secret_list.append(secret[i])
hidden_word = "_ " * len(secret_list)
clear_console()

while not win and not lost:
    guessed = False
    found = False

    while not guessed:
        print(man[wrong])
        print(f"you have already guessed {guessed_list}")
        print(f"you have {wrong} guesses remaining!")
        print(hidden_word)
        guess = input("Enter a letter: ")
        if len(guess) != 1 or accepted_characters.count(guess.lower()) != 1:
            clear_console()
            print("Enter a valid guess\n")
        elif guessed_list.count(guess) >= 1:
            clear_console()
            print(f"You have already guessed '{guess}'\n")
        else:
            guessed = True
            guessed_list.append(guess)
            guessed_list.sort()
    for i in range(len(secret_list)):
        if guess == secret_list[i]:
            temp_list = list(hidden_word)
            temp_list[((i + 1) * 2) - 2] = guess
            hidden_word = "".join(temp_list)
            point += 1
            found = True
    if found == False:
        wrong -=1
        clear_console()
        print("You guessed an incorrect letter, try again\n")
    else: clear_console()
    if wrong == 0:
        lost = True
    elif point == len(secret):
        win = True

if lost == True:
    clear_console()
    print(man[wrong])
    print(f"You lost!\nThe word was {secret}")

else:
    clear_console()
    print(man[wrong])
    print(f"congrats you win\nYou won with {wrong} guesses remaining!")
