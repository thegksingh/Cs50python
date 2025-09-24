import sys
import csv


def main():
    inputfile = check_len()
    inputfile, outputfile = check_filetype(inputfile)
    try:
        with open(inputfile, "r") as infile:
            reader = csv.DictReader(infile)
            with open(outputfile, "w", newline="") as outputfile:
                writer = csv.DictWriter(
                    outputfile, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {inputfile}")


def check_len():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        filename = sys.argv[1]
        return sys.argv[1]


def check_filetype(inputfile):
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
        return inputfile, outputfile
    else:
        sys.exit["Not a csv file"]


if __name__ == "__main__":
    main()
