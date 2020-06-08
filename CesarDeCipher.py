def CaesarDeCipher(cipher):
    text = ''
    for char in cipher:                 # loop through string
        if not char.isalpha():          # ignore everything not a letter
            continue
        char = char.upper()             # transform to uppercase
        code = ord(char) - 1            # shift letter code one lower
        if code < ord('A'):             # if arriving at A, wrap around to Z
            code = ord('Z')
        text += chr(code)               # add new decrypted text to output string
    print(text)

CaesarDeCipher(input('Enter your cryptogram: '))
