type = input("Input: ")
output = ""
for letter in type:
    if letter not in "AEIOUaeiou":
        output += letter
print(f"Output : {output}")
