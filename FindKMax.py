def partition(num, low, high):
    pivot = num[low]
    while low<high:
        while low<high and num[high]>pivot:
            high -= 1
        while low<high and num[low]<pivot:
            low += 1
        num[low], num[high] = num[high],num[low]
    num[low] = pivot
    return low

def quickSort(num, low, high):
    if low<high:
        index = partition(num, low, high)
        quicksort(num, low, index-1)
        quicksort(num, index+1, high)
    return num

def findkth(num, low, high, k):
    if low<high:
        index = partition(num, low, high)
        if index == k:
            return num[index]
        elif index < k:
            return findkth(num, index+1, high, k)
        else:
            return findkth(num, low, index-1, k)

 
 
pai = [2,3,1,5,4,6]
 
print(quicksort(pai, 0, len(pai)-1)) 
print(findkth(pai,0,len(pai)-1,3))

# https://blog.csdn.net/wenqiwenqi123/article/details/81669899
