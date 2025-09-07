#Ask the user for a number and print whether it’s odd or even.


number = int(input("waht's your number? "))
if number % 2 != 0:
    print("it's odd")
#we can even skip 8,9 line and edit line 11 to print it's even 
elif number % 2 == 0:
    print("it's even")  
else: 
    pritn("error")
