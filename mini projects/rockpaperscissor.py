import random
option = ["Rock" , "Paper" , "Scissor"]
userscore = 0
computerscore = 0
print("🎮 Welcome to Rock Paper Scissors!")
print("📜 Rules:")
print("1. You will play against the computer.")
print("2. Choices are: Rock ✊ , Paper ✋ , Scissors ✌️")
print("3. Rock beats Scissors (Rock crushes Scissors).")
print("4. Scissors beats Paper (Scissors cut Paper).")
print("5. Paper beats Rock (Paper covers Rock).")
print("6. If both choose the Scissor it's a Draw.")
print("7. First to win 2 out of 3 rounds is the Winner!")
print("8. Enter 'exit' to quit the game.")
while userscore < 2 and computerscore < 2:
    option = random.choice(option)
    userchoice = input("Rock ,Paper ,Scissor?  ")
    userchoice = userchoice.lower()
    if (userchoice == "rock" and option == "Scissor") or (userchoice == "paper" and option == "Rock") or (userchoice == "scissor" and option == "Paper"):
        userscore += 1
        print(f"You won!  Score {userscore} : {computerscore}")
    elif userchoice == option:
        print("Draw! ")
    else: 
        computerscore += 1
        print(f"You lost! Score {userscore} : {computerscore}")
    if userchoice == 2:
       print("Congratulation you won the game.")
    if computerscore == 2:
        print("Too bad you lost game. ")
    if userchoice == "exit":
        exit()
        
    



