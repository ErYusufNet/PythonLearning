# fizzbuzz.py

# 1'den 100'e kadar tüm sayılar üzerinde döngü oluşturuyoruz
for i in range(1, 101):

    # Hem 7'ye tam bölünüyorsa hem de içinde '7' geçiyorsa
    if i % 7 == 0 and '7' in str(i):
        print("FizzBuzz")

    # Sadece 7'ye tam bölünüyorsa
    elif i % 7 == 0:
        print("Fizz")

    # Sadece içinde '7' rakamı varsa
    elif '7' in str(i):
        print("Buzz")

    # Diğer tüm durumlarda sayının kendisini yazdır
    else:
        print(i)
