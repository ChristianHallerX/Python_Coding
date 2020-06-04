def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    dayslst = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year) == True:
        dayslst[1] = 29
    return dayslst[month-1]

def dayOfYear(year, month, day):
    month -= 1                      # adjust for zero indexing
    sum = 0                         # initialize variable
    
    for i in range(month):          # sum up all days in the months prior to month using function above
        sum += daysInMonth(year, i)
    return (sum + day)              # add sum of previous month's days to days in given month

print(dayOfYear(2000, 12, 31))
