list = {}
while True:
    try:
        type = input("").upper().strip()
        if type in list:
            list[type] += 1
        else:
            list[type] = 1
    except EOFError:
        for item in list:
            print(f"{list[item]} {item}")
        