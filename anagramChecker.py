def anagramChecker(string1,string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    return  print(list(string1).sort() == list(string2).sort())

anagramChecker("Listen","Silent")
