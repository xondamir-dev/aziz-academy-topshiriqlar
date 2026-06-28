# Bank hisobvaraqlarini boshqarish
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
hisobvaraqlar = []
for i in range(n):
    hisobvaraqt = input().split()
    hisobvaraqlar.append({'raqam': hisobvaraqt[0], 'egasi': hisobvaraqt[1], 'pul_miqdori': int(hisobvaraqt[2])})
    
u = 0 
for hisob in hisobvaraqlar:
    u += hisob['pul_miqdori']
    
print(f"Umumiy hisobvaraqlar soni: {n}")
print(f"Umumiy pul miqdori: {u}")