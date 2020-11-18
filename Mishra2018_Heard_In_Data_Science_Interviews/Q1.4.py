# How would you reverse the order of wordfs in a string in place? FOr example, if the input string is
# "i like this program very much", the function should return "much very program this like I".

def reversewords(string):
    for i in reversed(string.split(" ")):
        print(i, end=" ")


mystr = "i like this program very much"
reversewords(mystr)
