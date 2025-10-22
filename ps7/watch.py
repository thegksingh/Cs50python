import re
import sys

def main():
        print(prase(input("HTML: "))) 

def prase(s):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        iframe = match.group(1)
        return f"https://youtu.be/{iframe}"
    else:
         sys,exit()



if __name__ == "__main__":
    main()      