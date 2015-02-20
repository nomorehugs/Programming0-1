import time

today = time.strftime("%A")

print(today)

if today == "Friday":
    print("Today is Friday!")
else:
    print("It`s not Friday, it`s " + today)
