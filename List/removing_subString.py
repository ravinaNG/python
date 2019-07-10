mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"
ripited_list = ""
count = 0
while(count < len(mainStr)):
    ripited_list = ripited_list + mainStr[count]
    if(mainStr[count] == " "):
        substr = subStr + mainStr[count]
        if(ripited_list == substr):
            mainStr.replace(subStr, replacementStr)
            print (mainStr)
        ripited_list = ""
    count = count + 1
