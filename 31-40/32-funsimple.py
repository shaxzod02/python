
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def month_days(month, year):

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else: 
        return -1
    
def prev_date(day, month, year):

    if month < 1 or month > 12:
        return "Bunday oy mavjud emas"

    if day < 1 or day > month_days(month, year):
        return "Bunday sana mavjud emas"

    if day == 1 and month == 1:
        day = month_days(12, year - 1)
        month = 12
        year -= 1 

    elif day == 1 and month != 1:
        month -= 1
        day = month_days(month, year) 


    else:
        day -= 1

    return f"{day}/{month}/{year}"

print(prev_date(1, 3, 2020))           
print(prev_date(1, 1, 2020))           
print(prev_date(29, 2, 2019))  
  



            