# Bank uchun hisobvaraqlar balansini hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
balans = 0
for i in range(n):
    qoyilgan, olingan = map(int, input().split())
    balans += qoyilgan - olingan
print(balans)