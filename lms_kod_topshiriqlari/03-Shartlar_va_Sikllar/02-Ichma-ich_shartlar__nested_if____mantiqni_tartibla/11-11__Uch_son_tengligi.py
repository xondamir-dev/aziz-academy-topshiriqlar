
a, b, c = map(int, input().split())
if a == b and a == c and b == c:
    print("All equal")
else:
    print("Partially equal")