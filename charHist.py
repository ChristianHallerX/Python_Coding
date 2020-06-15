from os import strerror

srcname = input("Enter file name (.txt): ")
cnt = 0
letterDict = {}

try:
    sourcefile = open(srcname, 'rt')                               # open source file in read mode
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

try:
    targetfile = open(str(srcname[:-4]+".hist"), 'wt')      # open target file in write mode
except Exception as e:
    print("Cannot create destination file: ", strerr(e.errno))
    src.close()
    exit(e.errno)




try:
    text = sourcefile.read().lower()                 # read entire text and lowercase all
    for ch in text:
        if ch.isalpha():                     # only count alphabetical chars
            if ch not in letterDict:
                letterDict[ch] = 1           # if key does NOT exist yet, add to dict as value 1
                cnt += 1
            else:
                letterDict[ch] += 1          # if key exists, add one to value
                cnt += 1
        else:
            continue
    letterDict_tuples = list(letterDict.items())                    # change to list of tuples
    letterDict_tuples.sort(key = lambda x:x[1], reverse = True)     # lambda selects the second item
       
    print("Letters count: {}".format(cnt))
    for tuple in letterDict_tuples:
        targetfile.write("{} -> {}\n".format(tuple[0],tuple[1]))
        print("{} -> {}".format(tuple[0],tuple[1]))

except IOError as e:
    print("Cannot create target file: ", strerror(e.errno))
    exit(e.errno)

print("\nhist file sucessfully written.")
sourcefile.close()
targetfile.close()
