while True:
    fraction = input("Fraction : ")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or y == 0:
            continue

        percentage = (x / y) * 100
        if percentage >= 99 and percentage > 101:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        else:
            print(f"{percentage:.0f}%")
            break
    except ValueError:
        continue 
