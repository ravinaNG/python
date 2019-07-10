# this function for convrt in string list which user will give.
def convert_in_list(user):
    binary_list = []
    count = 0
    while count < len(user):
        binary_list.append(int(user[count]))
        count = count + 1
    return binary_list
# and this function for calculation that what is the number of users binari number.

def calculation(user_n):
    new_list = []
    sum = 1
    count = -1
    while count >= -len(user_n):
        if (user_n[count] == 0 or user_n[count] == 1):
            sum = sum + sum
            if (user_n[count] == 0):
                new_list.append(0)
            else:
                new_list.append(sum)
        else:
            print "Sorry your binary number is not binary number."
            break
        count = count - 1
    if len(user_n) == len(new_list):
        count = 0
        store = 0
        while (count < len(new_list)):
            store = store + new_list[count]
            count = count + 1
        return store

user = str(input("Enter your binary number for convert in number:- "))
user_n = convert_in_list(user)
number = calculation(user_n)
print number