import sys

total_lines =0
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2:
    if not sys.argv[1].endswith("py"):
        sys.exit("Not a Python file")     
    elif sys.argv[1].endswith(".py"):
        file_name = sys.argv[1]
        try:
            with open (file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue 
                    elif line.startswith("#"):
                        continue
                    else:
                        total_lines += 1
            print(total_lines)
        except FileNotFoundError:
            sys.exit("File does not exist")             

    

