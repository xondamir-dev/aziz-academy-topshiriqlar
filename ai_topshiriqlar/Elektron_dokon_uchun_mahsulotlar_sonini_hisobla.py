# Elektron do'kon uchun mahsulotlar sonini hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

mahsulotlar = {}
while True:
    try:
        s = input()
    except EOFError:
        break 
        
    if not s:
        break
        
    nom, son = s.split()
    son = int(son)
    
    if nom in mahsulotlar:
        mahsulotlar[nom] += son
    else:
        mahsulotlar[nom] = son
        
print(sum(mahsulotlar.values()))