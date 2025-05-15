#Digital clock
import time
my_time = int(input("enter the time: "))
for x in range(my_time, 0, -1):
    minutes = int(x / 60) % 60
    seconds = x % 60

    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("wake up")
