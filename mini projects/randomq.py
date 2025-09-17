import random

score = 0

def main():
    global score
    level = get_level()
    for i in range(10):
        x, y, arithmetic = get_question(level)
        answer = input(f"{x} {arithmetic} {y} = ")
        score = check(x, y, arithmetic, answer, score)
    print(f"Score: {score}")
        


def get_level():
    print("what level you wan5 to play,\n 1 for 0-9, 2 for 10-99 and so on up to 10.")
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level >= 1 and level <= 10:
                return level
        except ValueError:
            continue


def get_question(level):
    if level == 1:
        minnumber = 0
    else:
        minnumber = 10**(level - 1 )
    maxnumber = 10**level - 1
    x = random.randint(minnumber, maxnumber)
    y = random.randint(minnumber, maxnumber)
    arithmetic = random.choice(["+", "-", "*", "/"])
    return x, y, arithmetic


def check(x, y, arithmetic, answer, score):
    tries = 0
    try: 
        answer = float(answer)
    except ValueError:
        return score

    if arithmetic == "+":
        if answer == (x + y):
            score += 1
        else:
            tries += 1
    if arithmetic == "-":
        if answer == (x - y):
            score += 1
        else:
            tries += 1
    if arithmetic == "*":
        if answer == (x * y):
            score += 1
        else:
            tries += 1
    if arithmetic == "/":
        if answer == (x / y):
            score += 1
        else:
            tries += 1

    if tries == 3:
        print("wrong")
    return score 


if __name__ == "__main__":
    main()
