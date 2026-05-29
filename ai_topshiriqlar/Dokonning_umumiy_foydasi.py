# Do'konning umumiy foydasi
# Kurs: IT Dasturlash
# Mavzu: Arifmetik operatorlar, prioritet
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
mahsulotlar = list(map(int, input().split()))

umumiy_foyda = 0

for i in range(0, len(mahsulotlar), 2):
    narx = mahsulotlar[i]
    miqdor = mahsulotlar[i+1]
    umumiy_foyda += narx * miqdor
    
print(umumiy_foyda)