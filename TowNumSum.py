def towSum(L, target):
    d = {}
    for i in range(len(L)):
        if L[i] not in d:
            d[target - L[i]] = i 
        else:
            return d[L[i]], i
            
L = [1,3,5,6]
print(towSum(L, 7))
