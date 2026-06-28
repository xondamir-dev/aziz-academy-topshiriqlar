# O'quvchilarning o'rtacha bahosi
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
baholar = []
for i in range(n):
    baho = int(input())
    baholar.append(baho)

ortacha_baho = sum(baholar) / n 
print(ortacha_baho)