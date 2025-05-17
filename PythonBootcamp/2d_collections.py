fruits = ["apple", "banana", "cherry"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "meat"]
groceries = [fruits, vegetables, meats]
#print(groceries[1][1]) # list birlesiyor ve hangi listten hangi indexi yazdirmak istiyorsan
#for collection in groceries:
    #print(collection)
num_pad =((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()




