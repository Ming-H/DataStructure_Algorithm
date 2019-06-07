# -*- coding:utf-8 -*-

def partitions(num, low, high):
    pivot = num[low]
    while low<high:
        while low<high and num[high]>pivot:
            high -= 1
        while low<high and num[low]<pivot:
            low += 1
        num[low], num[high] = num[high], num[low]
    num[low] = pivot
    return low

def quick_sort(num, low, high):
    if low<high:
        pivot = partitions(num, low, high)
        quick_sort(num, low, pivot-1)
        quick_sort(num, pivot+1, high)
    return num

def findKmax(num, low, high, k):
    index = partitions(num, low, high)
    if index == k:
        return num[index]
    elif index < k:
        return findKmax(num, index+1, high, k)
    else:
        return findKmax(num, low, index-1, k)


def gen_pnext(p):
    ''' 生成针对指针p中各位置i的下一个检查的位置表，用于KMP算法 '''
    i,k=0,-1
    pnext = [-1 for i in range(len(p))]
    while i<len(p)-1:
        if k==-1 or p[i]==p[k]:
            i,k=i+1,k+1
            pnext[i]=k
            # 当 p[i] == p[k] 时，指针可以直接跳转到 k 位置
            if p[i]==p[k]:
                pnext[i]=pnext[k]
        else:
            k = pnext[k]
    return pnext

def match_kmp(t,p,pnext):
    i=0
    j=0
    while i<len(t) and j<len(p):
        if j==-1 or t[i]==p[j]:
            i,j=i+1, j+1
        else:
            j = pnext[j]
    if j == len(p):
        return i-j
    return -1


def gen_pnext(p):
    i,k=0,-1
    pnext = [-1 for i in range(len(p))]
    while i<len(p)-1:
        if k==-1 or p[i]==p[k]:
            i,k=i+1,k+1
            pnext[i]=k
            if p[i]==p[k]:
                pnext[i]=pnext[k]
        else:
            k=pnext[k]
    return pnext

def match_kmp(t, p, pnext):
    i=0
    j=0
    while i<len(t) and j<len(p):
        if j==-1 or t[i]==p[j]:
            i,j=i+1,j+1
        else:
            j=pnext[j]
    if j==len(p):
        return i-j
    return -1



def maxmin(l, low, high):
    if high-low<=1:
        return max(l[low], l[high]), min(l[low], l[high])
    mid = (low+high)//2
    left_list = maxmin(l, low, mid)
    right_list = maxmin(l, mid+1, high)
    if left_list[0] > right_list[0]:
        return left_list[0], min(left_list[1], right_list[1])
    else:
        return right_list[0], min(left_list[1], right_list[1])


def maxmin(l, low, high):
    if high-low<=1:
        return max(l[low], l[high]), min(l[low], l[high])
    mid = (low+high)//2
    left_list = maxmin(l, low, mid)
    right_list = maxmin(l, mid+1, high)
    if left_list[0]>right_list[0]:
        return left_list[0], min(left_list[1], right_list[1])
    else:
        return left_list[0], min(left_list[1], right_list[1])

def max_sum(L):
    thissum = 0
    maxsum = 0
    for item in L:
        thissum += item
        if thissum > maxsum:
            maxsum = thissum
        if thissum < 0:
            thissum = 0
    return maxsum


def heap_sort(array, k):
    def shiftdown(array, begin, end):
        i,j=begin, begin*2+1
        while j<end:
            if j+i<end and array[j+1]<array[j]:
                j += 1
            if array[i]<array[j]:
                break
            array[i], array[j] = array[j], array[i]
            i, j = j, j*2 + 1
    for i in range(len(array)//2-1, -1, -1):
        shiftdown(array, i, len(array))

    L = []
    for i in range(k):
        if i < len(array):
            L.append(array[0])
            array[len(array)-i-1], array[0] = array[0],\
                                         array[len(array)-i-1]
            shiftdown(array, 0, len(array)-i-1)
        else:
            break
    return L


def towSum(L, target):
    d = {}
    for i in range(len(L)):
        if L[i] not in d:
            d[target-L[i]] = i
        else:
            return d[L[i]], i

def sum_method(nums, start, path, result, target):
    if not target:
        return result.append(path)
    for i in range(start, len(nums)):
        if i>start and nums[i]==nums[i-1]:
            continue
        if nums[i]>target:
            break
        sum_method(nums, start+1, path+[nums[i]], \
                                result, target-nums[i])

def twosum(nums, target):
    nums.sort()
    result = []
    sum_method(nums, 0, [], result, target)
    return result


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
    
    
def solve_unique(vlist, wlist, totalWeight, totalLength):
    resArr = [0 for i in range(totalWeight+1)]
    for i in range(1, totalLength+1):
        for j in range(totalWeight, 0, -1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]


def edit(str1, str2):
    matrix = [[i+j for j in range(len(str2)+1)]\
                                        for i in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i-1][j]+1, \
                                matrix[i][j-1]+1, matrix[i-1][j-1]+d)
    return matrix[len(str1)][len(str2)]

def maxProduct(nums):
    tmp = nums[0]
    M = [0 for i in range(len(nums))]
    N = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        if i==0:
            M[i] = nums[i]
            N[i] = nums[i]
        else:
            M[i] = max(M[i-1]*nums[i],N[i-1]*nums[i], nums[i])
            N[i] = min(M[i-1]*nums[i], N[i-1]*nums[i], nums[i])
        tmp = max(tmp, M[i])
    return tmp


def binary_search(L, target):
    i = 0
    j = len(L)
    while i<=j:
        mid = (i+j)//2
        if L[mid]>target:
            j = mid-1
        elif L[mid]<target:
            i = mid+1
        else:
            return mid
    return False

def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1],L[j]
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

def merge(left, right):
    tmp = []
    i = 0
    j = 0
    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    if i == len(left):
        tmp.extend(right[j:])
    else:
        tmp.extend(left[i:])
    return tmp

def merge_srot(L):
    if len(L)<=1:
        return L
    mid = len(L)//2
    left = merge_srot(L[:mid])
    right = merge_srot(L[mid:])
    return merge(left, right)


def lcs(a, b):
    c = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    flag = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c[i+1][j+1] = c[i][j]+1
                flag[i+1][j+1] = 'ok'
            elif c[i+1][j]>c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                flag[i+1][j+1] = 'left'
            else:
                c[i+1][j+1] = c[i][j+1]
                flag[i+1][j+1]='up'
    return c, flag

def printlcs(flag, a, i, j):
    if i==0 or j == 0:
        return 
    if flag[i][j]=='ok':
        printlcs(flag, a, i-1, j-1)
        print(a[i-1], end='')
    elif flag[i][j]=='left':
        printlcs(flag, a, i, j-1)
    else:
        printlcs(flag, a, i-1, j)

def space_lcs(str_a, str_b):
    if len(str_a) == 0 or len(str_b) == 0:
      return 0
    max_len = 0
    lcs_str = ""
    dp = [0 for _ in range(len(str_b) + 1)]
    for i in range(1, len(str_a) + 1):
        left_up = 0
        for j in range(1, len(str_b) + 1):
            up = dp[j]
            if str_a[i-1] == str_b[j-1]:
                dp[j] = left_up + 1
                max_len = max(max_len, dp[j])
                if max_len == dp[j]:
                    lcs_str = str_a[i-max_len:i]
            else:
                dp[j] = 0
            left_up = up
    print(dp)
    print(max_len)
    return lcs_str


def longsetPalindrome(s):
    maxl = 0
    start = 0
    for i in range(len(s)):
        if i-maxl>=1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
            start = i-maxl -1
            maxl += 2
            continue
        if i-maxl >=0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
            start = i-maxl
            maxl += 1
    return s[start: start+maxl]


if  __name__ == "__main__":
    a='ABCBDAB'
    b='BDCABA'
    print(longsetPalindrome(a))











































