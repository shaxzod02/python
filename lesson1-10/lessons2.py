 
year = int(input("yilni kiriting" ))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(366)
else:
    print(365)    