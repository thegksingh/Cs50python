months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]
while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            a, b, c = date.split("/")
            a = int(a)
            b = int(b)
            c = int(c)
            if a <= 12 and b <= 31:
                print(f"{c:04}-{a:02}-{b:02}")
        elif "," in date:
            date = date.replace(",", "")
            x, y, z = date.split(" ")
            y = int(y)
            z = int(z)
            if x in months:
                i = months.index(x) + 1
                it y <= 31:
                    print(f"{z:04}-{i:02}-{y:02}")
    except ValueError:
        continue


