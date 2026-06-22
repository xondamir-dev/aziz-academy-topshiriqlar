# Bank hisobvaraqlari bo'yicha to'lovlar hisoboti
# Kurs: Dasturlash / IT
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

h, t, v = input().split()
t = int(t)
if v != "UZS" and t > 10000:
    s = t * 10 // 100 
else:
    s = 0 
u = t + s 
print(f"To'lov miqdori: {t} so'm, Soliq miqdori: {s} so'm, Umumiy miqdor: {u} so'm")