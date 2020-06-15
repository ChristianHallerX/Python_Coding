from os import strerror

srcname = input("Source file name (.txt): ")
cnt = 0
letterDict = {}
try:
    src = open(srcname, 'rt')
    ch = src.read().lower()                 # read entire text and lowercase all
    for i in ch:
        if i.isalpha():                     # only count alphabetical chars
            if i not in letterDict:
                letterDict[i] = 1           # if key does NOT exist yet, add to dict as value 1
                cnt += 1
            else:
                letterDict[i] += 1          # if key exists, add one to value
                cnt += 1
        else:
            continue
    src.close()

    letterTuples = letterDict.items()               # with .items() the dictionary becomes a list of tuples
    sorted_letterTuples = sorted(letterTuples)      # tuples on list get sorted alphabethically
    
    print("Letter count: {}\nLetters in {}: {}".format(cnt, srcname, sorted_letterTuples))

except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)
