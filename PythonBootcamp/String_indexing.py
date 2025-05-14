'''
accessing elements of sequence using [] (indexing operator)
[start : end : step]

'''
credit_number = "123456789"

print(credit_number[0:10:2])#0.indexten 10.indexe kadar 2 index atlayarak yazdirir
print(credit_number[2:])# bu durumda 2.indexten sonuna kadar yazdirir
last_digits = credit_number[-4:] # sadece son 4 rakami yazdiriyor
credit_number2 = credit_number[::-1]
print(f"XXX-XXXX-XXXX-{last_digits}")
print(credit_number2)