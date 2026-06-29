# Savdo markazi uchun mahsulotlarni sotuvi hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
jami = 0
for i in range(n):
    narx, miqdor = map(int, input().split())
    jami += narx * miqdor 

print(jami)