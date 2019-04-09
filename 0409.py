# -*- coding：utf-8 -*-

def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L
    
def insert_sort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i-1
        while j>=0 and L[j]>tmp:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp
    return L

def merge(a, b):
    i=0
    j=0
    tmp = []
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            tmp.append(a[i])
        else:
            tmp.append(b[j])
    if i==len(a):
        tmp.extend(b[j:])
    else:
        tmp.extend(a[i:])
    return tmp 

def merge_sort(L):
    if len(L)<2:
        return L
    mid = int(len(L)/2)
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

    
def partitions(nums, low, high):
    pivot = nums[0]
    while low<high:
        while low<high and nums[high]>pivot:
            high -= 1
        while low<high and nums[low]<pivot:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
    nums[low] = pivot
    return low

def quick_sort(nums, low, high):
    if low<high:
        index = partition(nums, low, high)
        quick_sort(nums, low, index-1)
        quick_sort(nums, index+1, high)
    return nums
    
def findkmax(num, low, high, k):
    if low<high:
        index = partition(num, low, high)
        if index == k:
            return num[index]
        elif index < k:
            return findkmax(num, index+1, high, k)
        else:
            return findkmax(num, low, index-1, k)
            
def maxsubseSum(L):
    thissum = 0
    maxsum = 0
    for item in L:
        thissum += item
        if thissum>maxsum:
            maxsum = thissum
        if thissum<0:
            thissum = 0
    return maxsum
        
def binary_search(L, item):
    i = 0
    j = len(L)-1
    while i<=j:
        index = int((i+j)/2)
        if L[index]>item:
            j = index - 1
        elif L[index]<item:
            i = index + 1
        else:
            return index
    return None
    
def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb+1)] for j in range(lena+1)]
    flag = c.deepcopy()
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i+1][j+1] = c[i][j] + 1
                flag[i+1][j+1] = 'OK'
            elif c[i+1][j]>c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                flag[i+1][j+1] = 'left'
            else:
                c[i+1][j+1] = c[i][j+1]
                flag[i+1][j+1] = 'up'
    return flag
    
def printlcsv(flag, a, i=len(a), j=len(b)):
    if i==0 or j==0:
        return None:
    if flag[i][j] == 'OK':
        printlcsv(flag, a, i-1, j-1)
        print(a[i-1], end='')
    elif flag[i][j] = 'left':
        printlcsv(flag, a, i, j-1)
    else:
        printlcsv(flag, a, i-1, j)
    
def maxProduct(nums):
    tmp = nums[0]
    M = [0 for i in range(len(nums))]
    N = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        if i==0:
            M[i] = nums[i]
            N[i] = nums[i]
        else:
            M[i] = max(max(M[i-1]*nums[i], N[i-1]*nums[i]), nums[i])
            N[i] = min(min(M[i-1]*nums[i], N[i-1]*nums[i]), nums[i])
        tmp = max(tmp, M[i])
    return tmp
    
    
