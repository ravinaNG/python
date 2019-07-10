color=["swati","soni","ravina","priya","ankita"]
count=0
big_1=[]
string=""
while (count<len(color)):
    counter=0
    while (counter<len(color[count])):
        if counter!=0 and counter!=4 and counter!=5:
            string=string+color[count][counter]
        counter=counter+1
    big_1.append(string)
    string=""
    count=count+1
print (big_1)