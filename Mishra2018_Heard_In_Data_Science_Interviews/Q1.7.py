# A message containing letters from A to Z is being encoded in numbers using the following mapping: A -> 1, B -> 2,...
# Z -> 26. Given an encoded message containing digits, how will you determine the total number of ways to decode it?
# For example, if input = 1234, the possible  decodings are: ABC, LC, AW. You can assume that the input contains only
# valid digits from 0 to 9. There are no leading 0's, no extra trailing 0's, and no two or more consecutive 0's.

def decodableletters(integers):

    # convert to string, since this offers options to iterate
    string = str(integers)

    # the length of the string as if all letters were single digits (edge case)
    allsingles = len(string)

    # record of detected letters
    counter = 0

    # the single letter counter is used to avoid counting single digits twice (pairwise singles vs allsingles)
    singlecounter = 0


    # sliding window through string in pairs, zipped means the numbers are still separated
    for pair in zip(string[::2], string[1::2]):

        # join the two numbers of a pair into string and convert to integer (easier for math)
        number = int("".join(pair))

        # if the number is larger than 26, then it can't be a one letter anymore, but must be two single letters
        if number > 26:
            counter += 2
            singlecounter += 2
        # if the pair number is smaller than 10, then the first digit must be 0 and the second one is a letter
        elif number < 10:
            counter += 1
        # if the number is zero, then it is not a letter
        elif number == 00:
            counter += 0
        # remaining is smaller than 26 and larger 10, then it's one letter
        else:
            counter += 1

    # sliding window pairs one digit offset
    for pair in zip(string[1::2], string[2::2]):
        number = int("".join(pair))
        if number > 26:
            counter += 2
            singlecounter += 2
        elif number < 10:
            counter += 1
        elif number == 00:
            counter += 0
        else:
            counter += 1

    # subtract the singlecounter from allsingles, otherwise we would count that twice
    result = allsingles - singlecounter + counter

    return result


example = 1234
testnumber = 19200125320821140718254632192125320615151209190846
testnumber2 = 239838383
print(decodableletters(example))
print(decodableletters(testnumber))
print(decodableletters(testnumber2))
