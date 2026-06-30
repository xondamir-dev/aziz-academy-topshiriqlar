# Tibbiyot markazi uchun bemorlar ro'yxatini boshqarish
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

while True:
    try:
        b = input()
    except EOFError:
        break 
    if b == "ro'yxat":
        print("Bemorlar ro'yxati:")
    elif b == "qo'shish":
        bs = input()
        print("Yangi bemor qo'shildi:", bs)
    elif b == "ozgartirish":
        bs = input()
        print("Bemor ma'lumotlari o'zgartirildi:", bs)
    elif b == "ochirish":
        bs = input()
        print("Bemor o'chirildi:", bs)