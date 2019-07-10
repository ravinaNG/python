scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
break_record = scores[0]
worst_record = scores[0]
highest_score = 0
lowest_score = 0
count = 1
while count < len(scores):
    if(scores[count] > break_record):
        highest_score =  highest_score + 1
        break_record = scores[count]
    if(scores[count] < worst_record):
        lowest_score = lowest_score + 1
        worst_record = scores[count]
    count = count + 1
print (highest_score, lowest_score)
