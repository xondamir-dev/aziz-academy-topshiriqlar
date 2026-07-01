# Bank hisobvaraqlari bo'yicha hisob-kitob dasturi
# Kurs: Dasturlash / IT
# Mavzu: input() bilan ishlash ⭐ — foydalanuvchidan ma'lumot olish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
u = 0
for i in range(n):
    hisob_raqami, foydalanuvchi_ismi, mablag = input().split()
    u += int(mablag)
    
print(f"Umumiy hisob: {u}")