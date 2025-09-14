# secret number fixed 45
print("welcome to the guess the number game :) ")
print(
    "Rule - You have to keeping guessing the number (integer) and will be provide hint like, too high/low, close. "
)
Attempts = 0
while True:
    number = int(input("Guess the number! "))
    Attempts += 1
    if number == 45:
        print(f"You guessed it right! \nTotal attempts = {Attempts}! ")
        break
    elif number >= 35 and number <= 55:
        print("close")
    elif number > 55:
        print("To high")
    elif number < 35:
        print("To low")


# secret number is random from 1 to 100
import random

print(
    "welcome to guess the number game! \nRule- You have to keep guessing the numbers until you find the secret number(1 to 100). \nYou only have 10 attempts"
)
guessnumber = random.randint(1, 100)
Attempts = 0
while True:
    number = int(input("Guess the number? "))
    Attempts += 1
    if number == guessnumber:
        print(f"You guess it right \nTotal attemptes = {Attempts}! ")
        break
    elif number > guessnumber - 10 and number < guessnumber + 9:
        print("Close enough")
    elif number >= guessnumber + 10:
        print("Too high")
    elif number <= guessnumber - 10:
        print("Too low")
    if Attempts == 10:
        print(f"Game over! \nNumber was {guessnumber}! ")
        break