mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over "
replacementStr = "on "
wordStr = ""
newStr = ""
count = 0
while(count < len(mainStr)):
    wordStr = wordStr + mainStr[count]
    if(count == len(mainStr) - 1):
        newStr = newStr + wordStr
        wordStr = ""
    elif(mainStr[count] == " "):
        # subStr = subStr + " "
        if (wordStr == subStr):
            newStr = newStr + replacementStr
            wordStr = ""
        else:
            newStr = newStr + wordStr
            wordStr = ""
    count = count + 1
print (newStr)

