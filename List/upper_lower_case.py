character = input("Enter a character: ")

lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
lowerCount = 0
upperCount = 0
digitCount = 0
nonAlphaCount = 0

for ch in character:
    for ch in lowerLetters:
        lowerCount += 1
    for ch in upperLetters:
        upperCount += 1
    for ch in digits:
        digitCount += 1
    else:
        nonAlphaCount += 1

if lowerCount > 0:
    print(character, "is a lower case letter.")
elif upperCount > 0:
    print(character, "is an upper case letter.")
elif digitCount > 0:
    print(character, "is a digit.")
elif nonAlphaCount > 0:
    print(character, "is a non-alphanumeric character.")
