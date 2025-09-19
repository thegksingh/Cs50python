import pyfiglet
import sys
import random


figlet = pyfiglet.Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))

elif len(sys.argv) == 1:
    text = input("Input: ").strip()
    font = random.choice(figlet.getFonts())
    figlet.setFont(font = font)
    print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")

