def CaesarCipher(text):
    cipher = ''
    for char in text:                   # loop through string
        if not char.isalpha():          # ignore everything not a letter
            continue
        char = char.upper()             # transform to uppercase letter
        code = ord(char) +1             # shift letter code one higher
        if code > ord('Z'):             # if arriving at Z, wrap around to A
            code = ord('A')
        cipher += chr(code)             # add new cipher letter to output string
    print(cipher)


CaesarCipher(input("Enter your message: "))
