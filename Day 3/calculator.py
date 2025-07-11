#simple calculator that can take integar, real number and float and perform addition, subtraction, divisions, amd multiplication.
print ("introducting you to simple calculator that i made.")


#addition 
#prompting user for input
x = float( input("let's do simple addition, what do you want to add: "))
y = float( input("to , "))
add =  float( x + y )

#print float value with two decimal places 
print (F"{add:.2f}")


#subtraction 
#prompting user for input 
a = float( input("now lets do simple subtraction, type a digit: "))
b = float( input(" "))
sub = float(a - b)

##print float value with two decimal places 
print (f"{sub:.2f}")


#division 
##promting user for input 
divide1 = float(input ("let's do division now, what do you want to divide: "))
divide2 = float(input("by: "))
div = float (divide1 / divide2 )
 
#print float value with two decimal places 
print (f"{div:.2f}")


#multiplication 
#prompting user for input 
multiply = float(input("why don't we try multiplying things now, what do you want to multiply: "))
multiply1 = float(input("to: "))
mult = float(multiply * multiply1)

#print float value with two decimal places 
print (f"{mult:.2f}")





#now we have written code the way that it will take add,subtract,divide or multiply as input and decide which thing to Perform accordingly. as for now it can Perform only one output of four at a time. To give another input you have to rerun the code.
#choosen a variable what whicn take input and if input if any one from add,subtract,divide or multiply it's run accordingly 
#firts its ask if value or variable is add,if yes then its run add run code
#if its not add then it check for subtract, if yes then it run subtract code
#if it not add or subtract it check for divde,if yes then it run divide code
#if its not anyone above three then it check for multiply, if yes it run multiply code
#and for some odd reason user decide not type anything esle then any four of these,it will print invalid input 
what = input("what do you want to do? add, subtract,divide or multiply ")
if what == "add":
        a1 = float( input("Okay let's do addition, what do you want to add: "))
        a2 = float(input("to: "))
        print (f"{a1 + a2:.2f}")

elif what == "subtract":
        s1 = float( input("why not let's do simple subtraction, what do you want to add: "))
        s2 = float( input("to , "))
        print (f"{s1 - s2:.2f}")

elif what == "divide":
    d1 = float(input ("As you say, what do you want to divide: "))
    d2 = float(input("by: "))
    print (f"{d1 / d2:.2f}")

elif what  == "multiply":
    m1 = float(input("Hmm that sound interesting, what do you want to multiply: "))
    m2 = float(input("to: "))
    print (f"{m1 * m2:.2f}")
else :
        print("invalid input")

print("Hope we meet again! ")

   

    








