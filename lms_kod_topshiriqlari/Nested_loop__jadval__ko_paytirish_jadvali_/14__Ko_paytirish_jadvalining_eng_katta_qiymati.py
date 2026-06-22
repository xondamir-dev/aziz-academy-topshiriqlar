n, m = map(int, input().split())
mx = 0 
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j > mx:
            mx = i * j 
print(mx)