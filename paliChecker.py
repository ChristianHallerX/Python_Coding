def paliChecker(string):
    string = string.lower().replace(" ", "")
    print(string == string[::-1])

paliChecker("Ten animals I slam in a net")
