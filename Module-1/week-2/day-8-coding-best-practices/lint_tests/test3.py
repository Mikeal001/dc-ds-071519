"""functioning"""
import string
SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
LETTER = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "encode":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = (LETTER.index(LETTER) +
                 SHIFT)
            ENCODED = ENCODED + LETTER[x]
if CHOICE == "decode":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTER.index(LETTER) - SHIFT
            ENCODED = ENCODED + LETTER[x]
print(ENCODED)
