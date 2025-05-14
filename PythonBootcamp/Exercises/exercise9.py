# Python Compound Interest Calculator (Bileşik Faiz Hesaplayıcı)

# Başlangıçta ana para (principal), faiz oranı (rate) ve süre (time) sıfır olarak tanımlanır
principal = 0
rate = 0
time = 0

# Kullanıcıdan geçerli (pozitif) bir ana para alınana kadar sorulmaya devam edilir
while principal <= 0:
    principal = float(input("Enter principal amount: "))  # float = ondalıklı sayı
    if principal <= 0:
        print("Principal amount must be greater than zero")

# Kullanıcıdan geçerli (pozitif) bir faiz oranı alınana kadar sorulmaya devam edilir
while rate <= 0:
    rate = float(input("Enter rate amount (in %): "))  # Örneğin: 5 yazarsa %5
    if rate <= 0:
        print("Rate amount must be greater than zero")

# Kullanıcıdan geçerli (pozitif) bir yıl süresi alınana kadar sorulmaya devam edilir
while time <= 0:
    time = int(input("Enter time in years: "))  # yıl cinsinden süre (örnek: 3 yıl)
    if time <= 0:
        print("Time can't be less than or equal to zero")

# Bileşik faiz formülü:
# A = P * (1 + r/100) ** t
# A = toplam para, P = principal, r = faiz oranı, t = yıl
# pow(x, y) → x üzeri y (üs alma işlemi yapar)

# (1 + rate / 100) → örneğin %5 faiz için 1.05 olur
# pow((1 + rate / 100), time) → bu değeri time kadar kendisiyle çarpar (üs alır)
# principal ile çarpılır → toplam para (faizli) elde edilir
total = principal * pow((1 + rate / 100), time)

# Sonuç yazdırılır – .2f kısmı: ondalıklı sayıyı 2 basamakla sınırlar (örnek: 1234.56)
print(f"Balance after {time} years is ${total:.2f}")
