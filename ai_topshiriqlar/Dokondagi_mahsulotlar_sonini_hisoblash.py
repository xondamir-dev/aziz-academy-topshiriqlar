# Do'kondagi mahsulotlar sonini hisoblash
# Kurs: Dasturlash / IT
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

j = 0
while True:
    try:
        mahsulot = input()
        n, s = mahsulot.split()
        j +=  int(s)
    except:
        break
        
print(f"Jami mahsulotlar soni: {j}")