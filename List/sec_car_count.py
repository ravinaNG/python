def count_caracter(user_str):
    count = 0 
    new_list = []
    small_list = []
    sum = 1
    while(count < len(user_str)):
        num = 0
        while (num < len(new_list)):
            if(user_str[count] == new_list[num][0]):
                count = count + 1
                break
            num = num + 1
        else:
            counter = count + 1
            while(counter < len(user_str)):
                if(user_str[count] == user_str[counter]):
                    sum = sum + 1
                counter = counter + 1
            small_list.append(user_str[count])
            small_list.append(sum)
            new_list.append(small_list)
            small_list = []
            sum = 1
        count = count + 1
    print (new_list)
    count = 0
    sec_max = 0
    max_num = 0
    caracter = 0
    while(count < len(new_list)):
        if(new_list[count][1] > max_num):
            max_num = new_list[count][1]
        if(max_num > new_list[count][1] > sec_max):
            sec_max = new_list[count][1]
            caracter = new_list[count][0]
        count = count + 1
    print (caracter, end = " :- ")
    print (sec_max)
count_caracter("antaatnnaxugaxa")