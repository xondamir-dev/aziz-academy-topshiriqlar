# Ishchilar uchun ish vaqti hisobla
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
i_b, i_t, s = map(int, input().split())
u = i_t - i_b 
if u > 8:
    q = u - 8 
else:
    q = 0  
    
q_h = q * s 
print(f"{u} soat, qo'shimcha haq {q_h}")