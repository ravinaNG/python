def add_numbers_print(number_x, number_y):
	number_sum = number_x + number_y
	print number_sum
sum4 = add_numbers_print(4, 5)
print sum4
print type(sum4)

def add_numbers_more(number_x, number_y):
	number_sum = number_x + number_y
	print "Hello from NavGurukul ;)"
	return number_sum
	number_sum = number_x + number_x
	print "Kya main yahan tak pahunchunga?"
	return number_sum
# Pehli return number_sum waali line se neeche aapne jo bhi code likha hai uss code mein se kuch bhi nahi chalega. Yeh isliye nahi chalega kyunki function chalate hue jab python ko ek return statement milti hai, toh python uss return statement ka use kar ke value return kar deta hai aur fir uske neeche wala koi bhi code nahi chalata hai.
sum6 = add_numbers_more(100, 20)
print sum6

def menu(day):
	if day == "monday":
		return "Butter Chicken"
	elif day == "tuesday":
		return "Mutton Chaap"
	else:
		return "Chole Bhature"
	print "Is it."
mon_menu = menu("monday")
print mon_menu
tues_menu = menu("tuesday")
print tues_menu
fri_menu = menu("friday")
print fri_menu


def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print "Kya main print ho payungi? :-("
    return food
    print "Lekin main toh pakka nahi print hounga :'("

mon_menu = menu("monday")
print mon_menu
tues_menu = menu("tuesday")
print tues_menu
fri_menu = menu("friday")
print fri_menu
