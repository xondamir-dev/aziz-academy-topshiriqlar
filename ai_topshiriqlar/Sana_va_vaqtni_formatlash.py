# Sana va vaqtni formatlash
# Kurs: IT Dasturlash
# Mavzu: Standart modullar: datetime
# Ball: 100
# Aziz Academy — AI Topshiriq

b, t = input().split()
h1, m1 = map(int, b.split(':'))
h2, m2 = map(int, t.split(':'))

s = h1 * 60 + m1
end = h2 * 60 + m2 

d = end - s 

soat = d // 60 
daqq = d % 60 

print(f"{soat} soat {daqq} daqiqa")