import pyfiglet
import sys
import random


f = pyfiglet.Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        text = input("Input: ").strip()
        if sys.argv[2] not in f.getFonts():
            sys.exit("Invalid usage")
        f.setFont(font=sys.argv[2])
        print(f.renderText(text))

elif len(sys.argv) == 1:
    text = input("Input: ").strip()
    f.setFont = random.choice(f.getFonts())
    print(f.renderText(text))

else:
    sys.exit("Invalid usage")
