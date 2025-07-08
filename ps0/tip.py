
def dollars_to_float(dollars): 
     dollars = dollars.replace ("$"," ")
     return float(dollars)

def percent_to_float(percent):
    percent = percent.replace ("%"," ")
    return float (percent )


def main ():
    dollars = dollars_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("what percentage would you like to tip? "))
    
    tip = dollars * (percent /100 )

    print (f"leave ${tip: .2f}")



main()