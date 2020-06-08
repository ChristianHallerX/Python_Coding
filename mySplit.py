def mysplit(strng):
    list = []
    word = ""
    for letter in strng:
        if letter.isspace() == False:   # if the letter is not a space, add to word
            word += letter
        elif word:
            list.append(word)           # if there is a space, then append the word to the list
            word = ""
            
    if word:                            # behind the last word is no space, so last word will have to get appended manually 
        list.append(word)
    
    return list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
