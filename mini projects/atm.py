print("Welcome to Pyatm \nEnter 'Exit' to exit Pyatm ")
money = 10000
for i in range(3):
    pin = input(f"Enter Pin. {3 - i} Attempts left \n")
    pin = pin.lower().replace(" ", "")
    if pin == "exit":
        print("Have a nice day! ")
        exit()
    if not pin.isdigit():
        print("Invalid input! ")
        continue
    numberpin = int(pin)
    if numberpin == 1234:
        print("Login Successfully! \n Enter 'Exit' to exit Pyatm. ")
        while True:
            print("1.Check Balance \n2.Deposite Money \n3.Withdraw Money.")
            option = input("")
            option = option.lower().replace(" ", "")
            if option == "checkbalance" or option == "1":
                print(f"Balance - {money}")
            elif option == "depositmoney" or option == "2":
                add = int(input("Amount - "))
                money += add
                print(f"{add} Successfully added to your account. \nBalance - {money}")

            elif option == "withdrawmoney" or option == "3":
                remove = int(input("Amount - "))
                if remove > money:
                    print("Insufficient Balance! ")
                else:
                    money -= remove
                    print(f"{remove} Successfully withdrawal. \nBalance - {money} ")
            elif option == "exit":
                print("have a nice day! ")
                exit()
