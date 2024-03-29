def gridTraveler(m,n,dict={}):
    key = str(m) + ',' + str(n)

    if (m == 1 and n == 1):
        return 1
    elif (m == 0 or n == 0):
        return 0
    elif key in dict.keys():
        return dict[key]

    dict[key] = gridTraveler(m-1,n,dict) + gridTraveler(m,n-1,dict)
    return dict[key]

def main():
    print(gridTraveler(1,1)) # 1
    print(gridTraveler(2,3)) # 3
    print(gridTraveler(3,2)) # 3
    print(gridTraveler(3,3)) # 6
    print(gridTraveler(18,18)) # 2333606220

if __name__ == '__main__':
    main()