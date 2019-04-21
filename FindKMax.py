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
    index = partition(num, low, high)
    if index == k:
        return num[index]
    elif index < k:
        return findkth(num, index+1, high, k)
    else:
        return findkth(num, low, index-1, k)
“”“
这个算法的算法复杂度是O(N)。
第一次交换，算法复杂度为O(N)，接下来的过程和快速排序不同，快速排序是要继续处理两边的数据，
再合并，合并操作的算法复杂度是O(1)，于是总的算法复杂度是O(N*logN)。但是这里在确定枢纽元
的相对位置（在K的左边或者右边）之后不用再对剩下的一半进行处理。也就是说第二次插入的算法复
杂度不再是O(N)而是O(N/2)，接下来的过程是1+1/2+1/4+........ < 2，换句话说就是一共是
O(2N)的算法复杂度也就是O(N)的算法复杂度。
”“”

 
 
pai = [2,3,1,5,4,6]
 
print(quicksort(pai, 0, len(pai)-1)) 
print(findkth(pai,0,len(pai)-1,3))

# https://blog.csdn.net/wenqiwenqi123/article/details/81669899

