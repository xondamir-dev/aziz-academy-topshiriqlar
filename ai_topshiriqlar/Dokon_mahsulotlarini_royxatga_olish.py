# Do'kon mahsulotlarini ro'yxatga olish
# Kurs: Dasturlash / IT
# Mavzu: break va continue — sikldan chiqish va o'tkazib yuborish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
jami = 0
for i in range(n):
    name, price = input().split()
    price = int(price)
    
    if price == 0:
        continue
    jami += price 
print(jami)