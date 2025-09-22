from tabulate import tabulate
import sys
import csv


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if not sys.argv[1].endswith("csv"):
        sys.exit("Not a csv file")
    elif sys.argv[1].endswith(".csv"):
        files = sys.argv[1]
        try:
            tabel = []
            with open(files, "r") as file:
                data = csv.reader(file)
                header = next(data)
                for row in data:
                    tabel.append(row)

            print(tabulate(tabel, headers=header, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exit")
