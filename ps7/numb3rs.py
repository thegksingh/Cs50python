import re
import sys

def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except:
        sys.exit()
def validate(ip):
    pattern =  (
        r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    )

    check = re.match(pattern, ip)
    if check:
        return True
    else:
        return False   

if __name__ == "__main__":
    main()        