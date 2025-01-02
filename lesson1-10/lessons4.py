day = int(input("Kinni kiriting"))
month = int(input("Oyni kiriting"))

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12:
    print("bunday oy yoq")
elif day < 1 and day > day_in_month[month-1]:
    print("bunday sana yoq")
else:
    if day == day_in_month[month-1]:
        month += 1
        day = 1 
    else:
         day += 1

    if month > 12:
        month = 1

    print(f"{day:02} {month:02}")                     

