import random

while True:
    level = input("Level: ")
    try:
        level = int(level)
        if level > 0:
            towin = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess == towin:
                        print("Just right!")
                        break
                    elif guess > towin:
                        print("Too large!")
                    else:
                        print("Too small!")
                except ValueError:
                    continue 
            break
    except ValueError:
        continue
