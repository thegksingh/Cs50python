import random
results = {}
score = 0
rolled = 0
totalscore = 0
print("🎲 Welcome to the Dice Roller with Statistics! 🎲")
print("Rules:")
print("1. You will roll TWO dice as many times as you choose.")
print("2. The sum of the two dice (2 - 12) will be recorded each time.")
print("3. At the end, you'll see how often each sum appeared and its probability.")
print("4. Special case: If you roll double ones (Snake Eyes 🎲🎲), you'll get a message!")
print("5. Finally, the program will show which sum appeared the most.")
print("6. Enter 'Exit' to quit.")
print("Enter 'Roll' to roll the dice.")
while True:
    roll = input("...").lower()
    if roll == "roll":
        rolled += 1
        dice1 = random.randint(1 ,6)
        dice2 = random.randint(1 ,6)
        score = dice1 + dice2
        totalscore += score 
        if score in results:
            results[score] += 1
        else:
            results[score] = 1
        print(f"🎲 = {dice1}. 🎲 = {dice2}")
        print(f"You rolled {rolled} times. \nScore is {score}! ")
        if dice1 == 1 and dice2 == 1:
            print("🐍Snake Eyes!!! ")
    if roll == "exit":
        print("Final result. ")
        for s in sorted(results.keys()):
                print(f"score {s}: {results[s]} times")
        print(f"Total score: {totalscore}.")
        print("Game over!")
        exit()

