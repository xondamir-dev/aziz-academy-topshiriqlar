n = int(input())
sonlar = list(map(int, input().split()))
print(*(son for son in sonlar if son % 5 == 0), sep='\n')