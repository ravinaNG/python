question_list = [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

options_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]

# Second question and thair option.
'''print "Q.", question_list[1]
print "1.", options_list[1][0]
print "2.", options_list[1][1]
print "3.", options_list[1][2]
print "4.", options_list[1][3]
'''
# this loop for print all the question and thair question.
'''count = 0
while count < len(question_list):
    print question_list[count]
    counter = 0
    number = 1
    while number <= len(options_list[count]):
        print number, options_list[count][counter]
        counter = counter + 1
        number = number + 1
    count = count + 1'''

# I modified this loop for ask to user that which option is write.
count = 0
one_time = 0
while count < len(question_list):
    print question_list[count]
    counter = 0
    number = 1
    while counter < len(options_list[count]):
        print number, options_list[count][counter]
        counter = counter + 1
        number = number + 1
    user = int(raw_input("(If you want 5050 then dile 5050 otherwise) Enter your answer here:- "))
    if user == 5050 and one_time == 1:
        print "You have took one time life line so now you can't use."
        user = int(raw_input("Enter your number:- "))
    elif user == 5050 and one_time == 0:
        one_time = 1
        print count+1, options_list[count][count]
        print solution_list[count], options_list[count][solution_list[count]-1]
        user = int(raw_input("Enter your answer:- "))
        if user == solution_list[count]:
            print " "
            print "***Congrats!*** your answer is right."
            print " "
        else:
            print " "
            print "##Sadly!## your answer is wrong."
            print "You are out from the game."
            break
    if(user == solution_list[count]):
        print " "
        print "***Congrats!*** your answer is right."
        print " "
    else:
        print " "
        print "##Sadly!## your answer is wrong."
        print "You are out from the game."
        break
    count = count + 1

