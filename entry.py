def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_feb(year):
    if(is_leap_year(year)):
        return 29
    return 28

def days_of_month(month):
    if(month % 2 == 0):
        return 30
    return 31

def days_in_month(month, year):
    if(month == 2):
        return days_in_feb(year)
    return days_of_month(month)



print(days_in_month(8, 1800))
