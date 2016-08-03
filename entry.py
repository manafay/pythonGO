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

def min_max(lst):
    min = lst[0]
    max = lst[0]
    for e in lst:
        if(e < min):
            min = e
        elif(e > max):
            max = e
    return [min, max]




def sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if( lst[j] > lst[j + 1]):
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst



def unique(lst):
    x = sort(lst)
    y = x[0]
    result = [y]
    for i in range(1, len(x)):
        if(x[i] > y):
            result.append(x[i])
            y = x[i]
    return result


print(days_in_month(8, 1800))

print(unique([4,9,1,6,3,7,56,786,89,45,3,5,7,6]))