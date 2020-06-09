def CaesarCipherPro(text,shift):
    import re
    text = str(text)
    cipher = ''
    
    if type(shift) == int:                              # check if shift is number
        if bool(re.match("^[A-Za-z0-9 ]*$", text)):     # check if text contains only allowed chars
            for char in text:                           # loop through string
                if char.isalpha():                      # process for letters
                    code = ord(char) + shift            # shift letter code by shift argument
                    if char.isupper():                  # A-Z wrap around for capital letters
                        if code > ord('Z'):             # if arriving at Z, wrap around to A
                            overshoot = code - ord('Z') - 1
                            code = ord('A') + overshoot
                    else:                               # a-z wrap around for lower case letters
                        if code > ord('z'):             # if arriving at z, wrap around to a
                            overshoot = code - ord('z')
                            code = ord('a') + overshoot - 1
                else:                                   # process for numbers -> leave as-is
                    code = ord(char)
                cipher += chr(code)                     # add new cipher letter to output string
            print(cipher)
            
        else:
            print("The text contains unallowed symbols.")
    else:
        print("The shift value has to be integer.")


CaesarCipherPro("The die is cast", 25)
