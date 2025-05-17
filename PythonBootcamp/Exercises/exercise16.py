'''seats = ((1, 2, "X"),
         (4, 5, "X"),
         (7, 8, "X"))
for row in seats:
    for seat in row:

        if seat == "X":
            print("Unaviable")
        else:
            print(f"Seat {seat} aviable ")'''
'''seats = (("X", "O", "P"),
         ("O", "O", "P"),
         ("X", "X", "P"))
for row in seats:
    for seat in row:
        if seat == "X":
            print("Seat not aviable")
        if seat == "O":
            print(f"Standart Seat {seat} aviable ")
        if seat == "P":
            print(f"Window Seat {seat} aviable ")
'''
# Koltuk haritası (3 satır, 3 sütun)
seats = (
    ("X", "O", "P"),
    ("O", "O", "P"),
    ("X", "X", "P")
)

# Kullanıcıdan satır ve sütun bilgisi alıyoruz
row = int(input("Lütfen satır numarasını girin (0-2): "))
col = int(input("Lütfen sütun numarasını girin (0-2): "))

# Seçilen koltuk
selected_seat = seats[row][col]

# Koltuk durumu kontrol ediliyor
print(f"Seçtiğiniz koltuk: {selected_seat}")

if selected_seat == "X":
    print("Seat not available ❌")
elif selected_seat == "O":
    print("Standard seat available ✅")
elif selected_seat == "P":
    print("Window seat available 🌟")
else:
    print("Bilinmeyen koltuk durumu.")

