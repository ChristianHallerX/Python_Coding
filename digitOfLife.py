def digitOfLife(string):
    string = str(string)                                    # make sure the input is a string
    string = string.replace(" ", "")                        # remove spaces
    strlist = list(string)                                  # convert string to list
    intlist = [int(i) for i in strlist]                     # convert list of strings to list of ints
    first_sum = sum(intlist)                                # sum of digits in list
    
    if first_sum > 10:
        print(sum([int(i) for i in list(str(first_sum))]))  # do the same as above in one line if the sum's result was two digits
    else:
        print(first_sum)


digitOfLife("19991229")
