# Kino teatrida chiptalar sonini hisoblash
# Kurs: Dasturlash / IT
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
f = 100
s = 120
t = f + s
if n <= f:
    print(f"Qoladi: {n}, Ketadi: 0")
elif n < t:
    print(f"Qoladi: {f}, Ketadi: {n-f}")
else:
    print(f"Qoladi: {t}, Ketadi: 0")