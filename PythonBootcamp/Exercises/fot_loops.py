# for loops = execute a block of code a fixed number of times
#you can iterate over a range,string,sequence
'''for x in (range(0, 21, 2)):
    print(x)
print("Happy new year!!!")'''
for x in range(1, 21):
    if x == 13: ## verdigimiz sayiyi atliayarak devam ediyor
        continue
    else:
        print(x)