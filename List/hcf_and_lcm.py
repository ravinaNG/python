def facter(number, sec_num):
    fact_list = []
    sec_fac_list = []
    count = 2
    while(count < number):
        if(number % count == 0):
            num = number / count
            fact_list.append(count)
            number = num
            count = 1
        count = count + 1
    number = int(number)
    fact_list.append(number)
    print (fact_list)
# *************************************
    count = 2
    while(count < sec_num):
        if(sec_num % count == 0):
            num = sec_num / count
            sec_fac_list.append(count)
            sec_num = num
            count = 1
        count = count + 1
    sec_num = int(sec_num)
    sec_fac_list.append(sec_num)
    print (sec_fac_list)
    if(number == sec_num):
            hcf = number
            lcm = number
            print (hcf)
            print (lcm)
    elif(len(sec_fac_list) > len(fact_list)):
        count = 0
        hcf = 1
        lcm = 1
        while (count < len(sec_fac_list)):
            if (count >= len(fact_list)):
                lcm = lcm * sec_fac_list[count]
                lcm = lcm * hcf
            elif (fact_list[count] == sec_fac_list[count]):
                hcf = hcf * fact_list[count]
            else:
                lcm = lcm * fact_list[count]
                lcm = lcm * sec_fac_list[count]

            count = count + 1
        print (hcf)
        print (lcm)
    else:
        print ("else : -  ")
        count = 0
        hcf = 1
        lcm = 1
        while (count < len(fact_list)):
            if (count >= len(sec_fac_list)):
                lcm = lcm * fact_list[count]
                lcm = lcm * hcf
            elif (fact_list[count] == sec_fac_list[count]):
                hcf = hcf * fact_list[count]
            else:
                lcm = lcm * fact_list[count]
                lcm = lcm * sec_fac_list[count]

            count = count + 1
        print (hcf)
        print (lcm)

user = int(input("Enter your first number:- "))
sec_user = int(input("Enter your second number:- "))
facter(user, sec_user)