"""
不稳定：选择排序、快速排序、希尔排序、堆排序
稳定：冒泡排序、插入排序、归并排序、基数排序

排序法	  平均时间	最差情形	稳定度	额外空间	备注
冒泡	O(n2)	    O(n2)	稳定	O(1)	n小时较好
选择	O(n2)	O(n2)	不稳定	O(1)	n小时较好
插入	O(n2)	O(n2)	稳定	O(1)	大部分已排序时较好
基数	O(logRB)	O(logRB)	稳定	O(n)	B是真数(0-9)，R是基数(个十百)
Shell	O(nlogn)	O(ns) 1<s<2	不稳定	O(1)	s是所选分组
快速	O(nlogn)	O(n2)	不稳定	O(nlogn)	n大时较好
归并	O(nlogn)	O(nlogn)	稳定	O(1)	n大时较好
堆	O(nlogn)	O(nlogn)	不稳定	O(1)	n大时较好
"""

#冒泡排序
"""
冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 
也就是说要进行n-1趟操作(已经归位的数不用再比较)
"""
def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[i]
    return L
    
#插入排序
"""
将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序
"""
def insert_sort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i-1
        while j>=0 and L[j]>tmp:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp
    return L

def insert_sort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i-1
        while j>=0:
            if L[j]>tmp:
                L[j+1] = L[j]
                L[j] = tmp
            j -= 1
    return L 
    
#快速排序
"""
将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序
"""   

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
        quickSort(num, low, index-1)
        quickSort(num, index+1, high)
    return num

arr = [ 12, 11, 13, 5, 6, 7] 
quickSort(arr, 0, len(arr)-1) 


def quick_sort(myList, start, end):
    if start < end:
        i,j = start,end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1
            myList[i] = myList[j]
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        myList[i] = base    #important, not (base = myList[j])
        quick_sort(myList, start, i - 1)
        quick_sort(myList, j + 1, end)
    return myList
      
nums = [9999,5,2,45,6,8,2,1]
print(quick_sort(nums, 0, len(nums)-1))
      
          
#归并排序
"""
首先归并排序使用了二分法，归根到底的思想还是分而治之。拿到一个长数组，将其不停的分为左边和右边两份，
然后以此递归分下去。然后再将她们按照两个有序数组的样子合并起来。
"""                 
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print merge_sort(a)
       
 参考文献：https://www.cnblogs.com/piperck/p/6030122.html 


#堆排序
"""
堆排序是一种选择排序，整体主要由构建初始堆+交换堆顶元素和末尾元素并重建堆两部分组成。
其中构建初始堆经推导复杂度为O(n)，在交换并重建堆的过程中，需交换n-1次，而重建堆的过程中，
根据完全二叉树的性质，[log2(n-1),log2(n-2)...1]逐步递减，近似为nlogn。所以堆排序时
间复杂度一般认为就是O(nlogn)级。
"""

def heapify(nums, n, i): 
    l = 2 * i + 1    # left = 2*i + 1 
    while l<n:
        if l+1<n and nums[l+1]>nums[l]:
            l += 1
        if nums[i] > nums[l]:
            break
        nums[i], nums[l] = nums[l], nums[i]
        i, l = l, 2*l+1

def heapSort(arr): 
    n = len(arr) 
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 

arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("排序后") 
for i in range(n): 
    print ("%d" %arr[i]),
