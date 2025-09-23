def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(text):
    output = ""
    for letter in text:
        if letter not in "AEIOUaeiou":
            output += letter
    return output

if __name__ == "__main__":
    main()