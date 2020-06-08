def digitdisplay(input):

    # create a dictionary with string digits as values and tuples of the five display rows
    dict = {
        '0': ('###', '# #', '# #', '# #', '###'),
        '1': ('  #', '  #', '  #', '  #', '  #'),
        '2': ('###', '  #', '###', '#  ', '###'),
        '3': ('###', '  #', '###', '  #', '###'),
        '4': ('# #', '# #', '###', '  #', '  #'),
        '5': ('###', '#  ', '###', '  #', '###'),
        '6': ('###', '#  ', '###', '# #', '###'),
        '7': ('###', '  #', '  #', '  #', '  #'),
        '8': ('###', '# #', '###', '# #', '###'),
        '9': ('###', '# #', '###', '  #', '###'),
        '.': ('   ', '   ', '   ', '   ', '  #')
    }

    # go through input string pull the ditionary value/digit
    digits = [dict[digit] for digit in str(input)]

    # digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc. 
    for i in range(5):                                      # repeat five times, once per line in the tuple
        print("  ".join(segment[i] for segment in digits))  # the join adds two spaces between each digit line
    

digitdisplay(input("Enter a number:"))
