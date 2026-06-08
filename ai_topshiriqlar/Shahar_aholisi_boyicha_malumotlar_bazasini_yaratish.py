# Shahar aholisi bo'yicha ma'lumotlar bazasini yaratish
# Kurs: IT Dasturlash
# Mavzu: input() bilan foydalanuvchidan ma’lumot olish
# Ball: 100
# Aziz Academy — AI Topshiriq

while True:
    d = input().strip()
    if d == '0':
        break
    parts = d.split()
    s = parts[0]
    a = parts[1]
    m = parts[2]
    
    print(f"{s} shahri aholisi: {a}, maydoni: {m}")