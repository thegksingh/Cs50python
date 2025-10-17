#Print numbers from 1 to 50, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")  
    elif i % 3 == 0 :
        print("Fizz")
    else:
        print(i)


