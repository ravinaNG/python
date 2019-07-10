ar = [3,2,1,3]
tallest_candles = 0
count = 0
totle = 0
while (count < len(ar)):
    if (ar[count] > tallest_candles):
        tallest_candles = ar[count]
    count = count + 1
count = 0
tallest_candel = (tallest_candles)
while (count < len(ar)):
    if ar[count] == tallest_candel :
        totle = totle + 1
    count = count + 1
print (totle)
