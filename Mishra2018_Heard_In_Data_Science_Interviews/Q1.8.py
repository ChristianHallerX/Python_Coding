# You are given a word document. How will you print all the unique words with frequencies? How will you find the top k
# ranked words along with their frequency?

def uniquewordranking(doc):
    # split words apart
    splitwords = doc.lower().replace(".", "").split()

    # create frequency list
    freqlist = []
    for word in splitwords:
        freqlist.append(splitwords.count(word))

    # fuse words and frequency, then create a dictionary
    freqdict = dict(list(zip(splitwords, freqlist)))

    # sort
    sorteddict = {k: v for k, v in sorted(freqdict.items(), key=lambda item: item[1])}

    for item in sorteddict.items():
        print(item)


document = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip" \
           "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
           "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia " \
           "deserunt mollit anim id est laborum lorem."

uniquewordranking(document)
