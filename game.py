"""A number-guessing game."""

# Put your code here
player_name = input("Howdy, What's your name? ")
print (player_name + ", I'm thinking of a number between 1 and 100")
print("Try to guess my number.")

import random
random_integer = random.randint(1,100)
number_of_attempts = 0

while True:
    guess = int(input("Your guess? "))
    if guess == random_integer:
        print(f'Well done {player_name}! You found my number in {number_of_attempts} tries!')
        break
    elif guess < random_integer:
        print("Your guess is too low, try again.")
        number_of_attempts += 1
    elif guess > random_integer:
        print("Your guess is too high, try again.")
        number_of_attempts += 1
        
    