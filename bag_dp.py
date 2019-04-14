def solve_unique(vlist,wlist,totalWeight,totalLength):
    """背包问题, 每个物品可用一次"""
    resArr = [0 for i in range(totalWeight+1)]
    for i in range(1,totalLength+1):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]

def solve_total(vlist,wlist,totalWeight,totalLength):
    """完全背包问题, 每个物品可无限次用"""
    resArr = [0 for i in range(totalWeight+1)]
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]
    
    
if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    print(solve_unique(v,w,weight,n))
    print(solve_total(v,w,weight,n))
    
    
参考文献：https://www.jianshu.com/p/25f4a183ede5
