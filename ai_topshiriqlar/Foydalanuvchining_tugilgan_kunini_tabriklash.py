# Foydalanuvchining tug'ilgan kunini tabriklash
# Kurs: IT Dasturlash
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

malumot = input().split()
isim = malumot[0]
tug_yil = int(malumot[1])
tug_oy = int(malumot[2]) 
tug_kun = int(malumot[3])

b = 15

if tug_kun >= b:
    print(tug_kun - b)
else:
    print(31 - b + 9)