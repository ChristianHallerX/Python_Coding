# Q1.1 Write a function to convert a string into integer.

def strint(mystring):
    if type(mystring) != str:
        print("Not a string.")
    elif not mystring.isnumeric():
        print("String contains non-numeric chars.")
    else:
        print(int(mystring))


strint(838399)
strint('ssasdf222')
strint('33335453')
