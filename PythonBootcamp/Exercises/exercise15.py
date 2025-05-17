#2d collections exercise
seats = ((1, 2, "X"),
         (4, 5, 6),
         ("X", 8, 9))
for seat in seats:
    for seat1 in seat:
        print(seat1, end= " ")
    print()