def main():
    while True:
        try:
            fraction = input("Fraction : ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue 

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    
    if y == 0:
        raise ZeroDivisionError()
    if x > y:
        raise ValueError()
    return int((x / y) * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"
    return p

if __name__ == "__main__":
    main()       

    
