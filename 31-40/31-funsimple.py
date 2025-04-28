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


def find_days(year, *month):
    day_list = [month_days(month, year) for month in month]
    return day_list

print(find_days(2020, 2, 11, 12))
print(find_days(2019, 2, 6, 7))
