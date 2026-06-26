n, m = map(int, input().split())
x = int(input())

f = False 

for i in range (1, n+ 1):
    for j in range(1, m + 1):
        if i * j == x:
            f = True 
            break 
        if f :
            break 
            
if f :
    print("Yes")
else:
    print("No")