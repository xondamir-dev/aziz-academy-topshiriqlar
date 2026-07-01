# Bank hisobvaraqlari bo'yicha foiz hisobi
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

m = float(input())

if m < 10000:
    f = m * 0.02 
elif m < 50000 and m > 10001:
    f = m * 0.03 
else:
    f = m * 0.04 
print(f)