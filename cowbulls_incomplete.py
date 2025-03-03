import random

def compare_numbers(number, user_guess):
    #SL Completed the code needed here
    cows = 0
    bulls = 0

    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls += 1
        elif user_guess[i] in number:
            cows += 1
    return cows,bulls  # SL Fixed 'cowbull' to 'cows,bulls'

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number #SL Fixed 0 to 1000 to get 4 digit number
guesses = 0
print(number) #SL Added parentheses() for print statement

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") # SL Replaced `raw_input` to `input`
    #SL Completed the code needed here
    if user_guess.lower() == "exit": #SL Changed 'user_guess' to 'user_guess.lower'
        break

    if len(user_guess) != 4 or not user_guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")
        continue

    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guess! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")

# Edited by Sinan Luckman