#kullanicidan kelime al ve icinde sesli harf kac tane var
word = input("enter a word: ")
vowels ="aeiouAEIOU"

count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"numer of vowels: {count}")