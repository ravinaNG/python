string_list = ["Ravina", "Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble", "Ravina"]
i=0
len_list=len(string_list)
new_list=[]
while(i<len(string_list)):
    j=i+1
    while(j<len(string_list)):
        if(string_list[i]==string_list[j]):
            new_list.append(string_list[i])
            x= string_list[i]
            y= string_list[j]
            string_list.remove(x)
            string_list.remove(y)
            j=0
            i=0
        if(j==len(string_list)-1):
            new_list.append(string_list[i])
            a = string_list[i]
            string_list.remove(a)
            i = 0
            j = 0
        j=j+1
    i=i+1
print (new_list)