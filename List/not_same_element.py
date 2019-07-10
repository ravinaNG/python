def check_interation(listA, listB):
	lengthA = len(listA)
	lengthB = len(listB)
	checkA = 0
	
	none_repited_list = []
	while(checkA < lengthA):
		checkB = 0
		while(checkB < lengthB):
			if(listA[checkA] != listB[checkB]):
				none_repited_list.append(listA[checkA])
				# print none_repited_list
			checkB = checkB + 1
		checkA = checkA + 1
		
	return none_repited_list

checking_intersection = check_interation([1,5,10,12,16,20], [1,2,10,13,16])
print checking_intersection 
