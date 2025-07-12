greet = input ("Greaating: ").strip()
if greet.lower().startswith("hello"):
    print("$0")
elif greet.lower().startswith("h"):
    print("$20")
else:
    print("$100")