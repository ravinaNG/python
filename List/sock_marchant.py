def sockMerchant(n, ar):
    index = 0
    pair_of_colour = 0
    while(index < n):
        pair_index = index + 1
        while(pair_index<n):
            if(ar[index] == ar[pair_index]):
                pair_of_colour = pair_of_colour + 1
                a = ar[index]
                b = ar[pair_index]
                ar.remove(a)
                ar.remove(b)
                index = 0
                pair_index = 0
                n = len(ar)
            pair_index = pair_index + 1
        index = index + 1
    return pair_of_colour

n = 10
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
print (sockMerchant(n, ar))
