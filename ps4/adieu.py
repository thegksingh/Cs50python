import inflect

p = inflect.engine()
lists = []
while True:
    try:
        name = input("Name: ")
        lists.append(name)
    except EOFError:
        break
print("Adieu, adieu, to", p.join(lists))