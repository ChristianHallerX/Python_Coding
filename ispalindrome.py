def isPali(mystr):
    if type(mystr) is not str:
        return None

    left = 0
    right = len(mystr) -1

    while left < right:
        if mystr[left] != mystr[right]:
            return False
        left += 1
        right -= 1
    
    return True

#print(isPali('mom')) # True
#print(isPali('hello')) # False
#print(isPali('')) # True
#print(isPali(123)) # None because int
