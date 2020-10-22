def pythagotrip1(list):
    '''Returns yes if list contains a Pythagorean triplet'''

    for a in list:
        for b in list:
            for c in list:
                if (a**2 + b**2) == c**2:
                    flag = True
    if flag:
        print('Yes')
    else:
        print('No')
    
