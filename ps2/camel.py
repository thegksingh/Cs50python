text = input("Camelcase : ")
result = ""
for i,letter in enumerate(text):
    if letter.isupper() and i != 0:
        result += "_" + letter.lower()
    else:
        result += letter.lower()
print(f"Snake_case : {result} ")