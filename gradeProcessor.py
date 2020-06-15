from os import strerror

srcname = input("Enter file name (.txt): ")
studentDict = {}

try:
    sourcefile = open(srcname, 'rt')                               # open source file in read mode
    #sourcefile = open("grades.txt", 'rt')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

try:
    destinationfile = open("processedGrades.txt", 'wt')            # open target file in write mode
except Exception as e:
    print("Cannot create destination file: ", strerr(e.errno))
    src.close()
    exit(e.errno)




try:
    lines = sourcefile.read().splitlines()                          # read entire text
    for line in lines:
        words = line.split("\t")                                    # Creates a list of words

        name = words[0] + " " + words[1]                            # Combines first and last name from words

        points = float(words[2])                                    # Selects and changes type from str to float

        before = studentDict.setdefault(name, 0)                    # Checks whether the student with the Name in variable name is already in the dictionary and if yes, saved his current number of points to bef; if not then bef will be set to 0

        studentDict[name] = before + points                         # Write a dictionary with summarized points

    studentTuples = studentDict.items()                             # Sorting names alphabetlically. With .items() the dictionary becomes a list of tuples
    sorted_studentTuples = sorted(studentTuples)                    # Tuples on list get sorted alphabethically
    
    for tuple in sorted_studentTuples:                              # print and write tuble by tuple  
        print(str(tuple[0])+ "\t" + str(tuple[1]))
        destinationfile.write(str(tuple[0]) + "\t" + str(tuple[1]) + "\n")
    

except IOError as e:
    print("Cannot create target file: ", strerror(e.errno))
    exit(e.errno)

print("\nGrade-processing file 'processedGrades.txt' sucessfully written.")
sourcefile.close()
destinationfile.close()
