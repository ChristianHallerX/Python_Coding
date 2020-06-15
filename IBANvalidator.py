# IBAN Validator

def IBANvalidator(iban):                                        # the first part is mainly about checking, processing happens in the else section.
    iban = iban.replace(' ','')                                 # remove all spaces
    
    if not iban.isalnum():                                      # check if invalid symbols are in the string
        print("You have entered invalid characters.")
    elif len(iban) < 15:                                        # the IBAN cannot be shorter than the shortest recognized number
        print("IBAN entered is too short.")
    elif len(iban) > 31:                                        # cannot be longer than the longest recognized
        print("IBAN entered is too long.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()                   # create a new string, with the old string's digits first and the old capitalized letters at the end
        iban2 = ''
        for ch in iban:
            if ch.isdigit():                                    # loop through string and add all digits at the beginning of the string in new variable
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))           # when arriving at letters, add coding to letters and combine with digits
        ibann = int(iban2)
        
        if ibann % 97 == 1:                                     # calculate modulus when dividing encoded iban through 97. Passed if modulus result is 1
            print("IBAN entered is valid.")
        else:
            print("IBAN entered is invalid.")
        
IBANvalidator(input("Enter IBAN, please: "))
