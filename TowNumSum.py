def func(L, target):
    d = {}
    for item in L:
        if item in d:
            print(item, d[item])
        else:
            d[target-item] = item
    
L = [1,2,3,4,5,6]
func(L, 9)
