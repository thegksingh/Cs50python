a = input("Expression: ")
x, y ,z =a.split(" ")
x = int(x)
z = int(z)
if y == "+":
   print(f"{x + z:.1f}")
elif y == "-":
   print(f"{x - z:.1f}")
elif y == "*":
   print(f"{x * z:.1f}")
elif y == "/":
   print(f"{x / z:.1f}")
