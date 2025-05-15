import time
'''
my_time = int(input("enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
print("Hey wake up") 

sec = int(input("enter time in seconds: "))
for x in range(sec, -1, -1):
    print(x)
    time.sleep(1)
print("Hey wake up")

text = input("enter text: ")

for char in text:
    print(char, end="", flush=True)
    time.sleep(1)
print("\ndone!")'''
text = input("enter word: ")
vowels="aeiouAEIOU"
vowels_count = 0
count = 0
vowels_characters =""

for char in text :
    print(char, end="", flush=True)
    time.sleep(1)
    count += 1
    if char in vowels:
        vowels_count += 1
        vowels_characters += char
print(f"\ntotal characters: {count}")
print(f"number of vowels: {vowels_count}")


if vowels_count == 0:
    print("no vowels")
else:
    print(f"Vowels found: {vowels_count}")




