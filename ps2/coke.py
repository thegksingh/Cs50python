due = 50
while True:
    print(f"Amount Due: {due}")
    inserts = int(input("Insert Coin: "))
    if inserts in [5, 10, 25]:
        due -= inserts 
    if due <= 0:
        print(f"Changed owed: {abs(due)}")
        break
