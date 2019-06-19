#-*- doding:utf-8 -*-

def partitions(num, low, high):
	pivot = num[low]
	while low<high:
		while low<high and pivot<num[high]:
			high -= 1
		while low<high and pivot>num[low]:
			low += 1
		low, high = high, low
	num[low] = pivot
	return low

def quicksort(num, low, high):
	if low<high:
		index = partitions(num, low, high)
		quicksort(num, low, index-1)
		quicksort(num, index+1, high)
	return num

def findkmax(num, low, high, k):
	index = partitions(num, low, high)
	if index == k:
		return num[index]
	elif index < k:
		return findkmax(num,index+1, high, k)
	else:
		return findkmax(num, low, index-1, k)

def partition(num, low, high):
	pivot = num[low]
	while low<high:
		while low<high and pivot<num[high]:
			high -= 1
		while low<high and pivot>num[low]:
			low += 1
		num[low], num[high] = num[high], num[low]
	num[low] = pivot
	return low

def partitions(num, low, high):
	pivot = num[low]
	while low<high:
		while low<high and pivot<num[high]:
			high -= 1
		while low<high and pivota>num[low]:
			low += 1
		num[low], num[high] = num[high], num[low]
	num[low] = pivot
	return low



def gen_pnext(p):
	i, k = 0, -1
	pnext = [-1 for i in range(len(p))]
	while i<len(p)-1:
		if k==-1 or p[i]==p[k]:
			i,k = i+1,k+1
			pnext[i] = k
			if p[i] == p[k]:
				pnext[i] = pnext[k]
		else:
			k = pnext[k]
	return pnext

def match_kmp(t,p,pnext):
	i=0
	j=0
	while i<len(t) and j<len(p):
		if j==-1 or t[i]==p[j]:
			i, j = i+1, j+1
		else:
			j = pnext[j]
	if j==n:
		return i-j
	return -1

def gen_next(p):
	i, k = 0, -1
	pnext = [-1 for i in range(len(p))]
	while i<len(p)-1:
		if k==-1 or p[i]==p[k]:
			i,k=i+1,k+1
			pnext[i] = k
			if p[i]==p[k]:
				pnext[i] = pnext[k]
		else:
			k = pnext[k]
	return pnext

def match_kmp(t, p, pnext):
	i = 0
	j = 0
	while i<len(t) and j<len(p):
		if j==-1 or t[i]==p[j]:
			i,j=i+1,j+1
		else:
			j=pnext[j]
	if j==len(p):
		retiurn i-j
	return -1


def gen_pnext(p):
	i,k = 0,-1
	pnext = [-1 for i in range(len(p))]
	while i<len(p)-1:
		if k==-1 or p[i]==p[k]:
			i,k=i+1,k+1
			pnext[i] = k
			if p[i] == p[k]:
				pnext[i]=pnext[k]
		else:
			k = pnext[k]
	return pnext


def match(t, p, pnext):
	i = 0
	j = 0
	while i<len(t) and j<len(p):
		if j==-1 or t[i]==p[j]:
			i,j=i+1,j+1
		else:
			j = pnext[j]
	if j == len(p):
		return i-j
	return -1



def maxmin(l, low, high):
	if high-low<=1:
		return max(l[low], l[high]), min(l[low], l[high])
	mid = (low+high)//2
	left_list = maxmin(l, low, mid)
	right_list = maxmin(l, mid, high)
	if left_list[0]>right_list[0]:
		return left_list[0], min(left_list[1], right_list[1])
	else:
		return right_list[0], min(left_list[1], right_list[1])

def maxmin(l, low, high):
	if high-low<=1:
		return max(l[low], l[high]), min(l[low], l[high])
	mid = (low+high)//2
	left_list = maxmin(l, low, mid)
	right_list = maxmin(l, mid, high)
	if left_list[0] > right_list[0]:
		return left_list[0], min(left_list[1], right_list[1])
	else:
		return right_list[0], min(left_list[1], right_list[1])

def subsum(L):
	thissum = 0
	maxsum = 0
	for item in L:
		thissum += item
		if thissum>maxmin:
			maxsum = thissum
		if thissum < 0:
			thissum = 0
	return maxsum

def heap_sort(array, k):
	def siftdown(array, begin, end):
		i, j = begin, begin*2+1
		while j<end:
			if j+1<end and array[j+1]<array[j]:
				j += 1
			if array[i]<array[j]:
				break
			array[i], array[j] = array[j], array[i]
			i,j=j,j*2+1

	for i in range(len(array)//2-1, -1, -1):
		siftdown(array, i, len(array))

	li = []
	for i in range(k):
		if len(array)>i:
			li.append(array[0])
			array[len(array)-1-i], array[0] = array[0], array[len(array)-1-i]
			siftdown(array, 0, len(array)-1-i)
		else:
			break
	return li

def heap_sort(array,k):
	def shiftwodm(array, begin, end):
		i,j=begin, begin*2+1
		while j<end:
			if j+1<end and array[j+1]<array[j]:
				j += 1
			if array[i] < array[j]:
				break
			array[i], array[j] = array[j], array[i]
			i, j = j, j*2+1

	for i in range(len(array)//2-1, -1, -1):
		shiftwodm(array, i, len(array))

	li = []
	for i in range(k):
		if len(array)>i:
			li.append(array[0])
			array[len(array)-1-i], array[0] = array[0], array[len(array)-1-i]
			shiftwodm(array, 0, len(array)-1)
		else:
			break
	return li


























