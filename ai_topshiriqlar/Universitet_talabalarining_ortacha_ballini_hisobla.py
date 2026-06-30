# Universitet talabalarining o'rtacha ballini hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
balls = list(map(int, input().split()))

print(sum(balls) / n)