import re
import sys

def main():
    print(convert(input("Hours: ")))
        
def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s(AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError

    h1, m1, mer1, h2, m2, mer2 = match.groups()
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)

    if h1 > 12 or h2 > 12 or m1 >= 60 or m2 >= 60:
        raise ValueError

    h1 = to_24_hour(h1, mer1)
    h2 = to_24_hour(h2, mer2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def to_24_hour(hour, meridian):
    if meridian == "AM":
        return 0 if hour == 12 else hour
    else:
        return hour if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
