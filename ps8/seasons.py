from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birth_str = input("Date of Birth: ").strip()
    try:
        year, month, day = map(int, birth_str.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    days_alive = (today - birth_date).days
    minutes_alive = days_alive * 24 * 60
    words = p.number_to_words(minutes_alive, andword="").capitalize()
    print(f"{words} minutes")

if __name__ == "__main__":
    main()