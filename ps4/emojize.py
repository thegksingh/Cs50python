import emoji


asked = input("Input: ")
emo = emoji.emojize(asked, language = "alias")
print(f"Output: ", emo)

