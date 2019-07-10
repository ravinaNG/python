user = "uddduduu"
sum = 0
up = 1
down = 1
count = 0
while(count < len(user)):
    if (user[count] == "u"):
        if(user[count-1] == "d" ):
            up = 1
        up = up + 1
        down = 1
    if(user[count] == "d"):
        if(user[count-1] == "u"):
            down = 1
        down = down + 1
    if(up > 0 and down > 0 and up == down):
        sum = sum + 1
        up = 1
        down = 1
    count = count + 1
print (sum)
