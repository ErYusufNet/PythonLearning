#Dictionaries = collection of {key:value}

capitals = {"Finland": "Helsinki",
            "England": "London",
            "France": "Paris"}
'''country = capitals.keys()
capital = capitals.values()
for key in country:
    print(key)

for cap in capital:
    print(cap)
'''
for key, value in capitals.items():
    print(f"{key}: {value}")
