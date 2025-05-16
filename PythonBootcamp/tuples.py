#tuple = () sıralı ve değiştirilemez. Kopya değerlere izin verir. Listeye göre daha hızlı çalışır.

fruits = ("apple", "orange", "banana", "banana")
for fruit in fruits:
    print(fruit)

print(fruits.index("apple"))
print(fruits.count("banana"))

