a = input()
b = a.split(",")
if len(b) == 2:
    print(f"Name: {b[0].strip()}")
    print(f"Age: {b[1].strip()}")