#nested loop= a loop within another loop(outer,inner)
#outer loop:
#   inner loop:
rows = input("enter the # of rows: ")
columns = int(input("enter # of columns: "))
symbol = input()

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()