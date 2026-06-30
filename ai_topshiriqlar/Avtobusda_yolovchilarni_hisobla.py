# Avtobusda yo'lovchilarni hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    n = n - a + b 
    
print(n)