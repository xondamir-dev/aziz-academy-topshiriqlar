# Maktab kutubxonasidagi kitoblar katalogini tuzish
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
for i in range(n):
    kitob = input().split()
    print(f"{kitob[0]} - {kitob[1]} - {kitob[2]}")