# Kitob do'konidagi kitoblar sonini hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
kitoblar = []
for i in range(n):
    kitoblar.append(int(input()))
    
u = sum(kitoblar)
print(u)