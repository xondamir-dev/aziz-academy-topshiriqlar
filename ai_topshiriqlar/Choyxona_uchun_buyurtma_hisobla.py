# Choyxona uchun buyurtma hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

while True:
    try:
        ch = input()
        m = int(input())
        n = float(input())
        
        if m < 10:
            c = n * 0.10 
        else:
            c = n * 0.05 
        print(ch)
        print(m)
        print(n)
        print(c)
    except EOFError:
        break