# Matnni qayta ishlash
# Kurs: Dasturlash / IT
# Mavzu: Ma’lumot turlari: str (string) kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
input_str = input().split()
ism = input_str[0]
familiya = input_str[1]
tugilgan_yili = int(input_str[2])

joriy_yil = 2023 
yosh = joriy_yil - tugilgan_yili
print(ism + " " + familiya, yosh)