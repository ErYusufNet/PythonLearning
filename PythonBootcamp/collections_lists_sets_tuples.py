'''
collection = birden fazla değeri saklamak için kullanılan tek bir "değişken"

lists = [] sıralı ve değiştirilebilir. Kopya değerlere (aynı eleman) izin verir.

set = {} sırasız ve değiştirilemez (ancak eleman ekleme/silme yapılabilir). Kopya elemanlara izin vermez.

tuple = () sıralı ve değiştirilemez. Kopya değerlere izin verir. Listeye göre daha hızlı çalışır.

'''
#list
fruits = ["apple", "orange", "banana", "cherry"]
#fruits[0] = "pineapple"

#fruits.insert(0,"elma")
fruits.sort()
fruits.reverse()
print(fruits)






'''for fruit in fruits:
    if fruit == "apple":
        print("red apple")
    else:
        print(fruit)'''