def readint(prompt, min, max):
    try:
        v = int(input(prompt))
        assert min < v < max
        return v
    except AssertionError:
        print("Error: the value is not within permitted range ({}..{})".format(min,max))
    except:
        print("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
