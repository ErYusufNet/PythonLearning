x = [4, 'hi', True]
x.append('car') #listin sonuna ekleme yapar
x.extend([4,3,2,1,'house']) #ikinci list olarak atandigi listin devamina gelir
#x.pop(1) #index numarasiyla verileni siler 
x[1] = 'good bye'
y = [3]
print(len(x))
print(len(y))
print(x)