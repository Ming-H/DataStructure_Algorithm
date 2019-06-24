def qselect(A,k): 
  if len(A)<k:return A 
  pivot = A[-1] 
  right = [pivot] + [x for x in A[:-1] if x>=pivot] 
  rlen = len(right) 
  if rlen==k: 
      return right 
  if rlen>k: 
      return qselect(right, k) 
  else: 
      left = [x for x in A[:-1] if x<pivot] 
      return qselect(left, k-rlen) + right 
  
print(qselect([11,8,4,1,5,2,7,9], 5))

#https://www.jb51.net/article/86764.htm




"""
可以利用数据结构的最小堆来处理该问题。
对于每个非叶子节点的数值，一定不大于孩子节点的数值。这样可用含有K个
节点的最小堆来保存K个目前的最大值(当然根节点是其中的最小数值)。
每次有数据输入的时候可以先与根节点比较。若不大于根节点，则舍弃；
否则用新数值替换根节点数值。并进行最小堆的调整。
"""

def heap_sort(ary, k):
    # 构建小顶堆
    def siftdown(ary, begin, end):
        i,j = begin, begin*2+1
        while j < end:
            if j+1 < end and ary[j+1] < ary[j]:  # 查看左右子树的最小节点
                j += 1
            if ary[i] < ary[j]:  # 如果不需要交换了，则停止
                break
            ary[i],ary[j] = ary[j],ary[i]  # 交换父和子
            i,j = j,j*2+1

    # 构建最小堆
    end = len(ary)
    for i in range(end//2-1, -1, -1):
        siftdown(ary,i, end)
    print('小顶堆',ary)


    # 提取k个元素。每提取一个元素，构建一遍最小堆
    li = []
    for i in range(k):
        if len(ary) > i:
            li.append(ary[0])  # 取出最小的
            ary[end - 1 - i],ary[0] = ary[0],ary[end-1-i]  #最后一个与第一个交换。这里只是假设这么一步。
            siftdown(ary, 0, end-1-i)  # 重新建堆,不考虑最后一个
        else:
            break
    return li



if __name__ == '__main__':
    a = [4,5,1,6,2,4,7,8,7,3,8]
    k = 5
    print(heap_sort(a,k))


"""
第二部分、处理海量数据问题之六把密匙
密匙一、分而治之/Hash映射 + Hash_map统计 + 堆/快速/归并排序

密匙二、多层划分
多层划分—-其实本质上还是分而治之的思想，重在“分”的技巧上！ 
适用范围：第k大，中位数，不重复或重复的数字 
基本原理及要点：因为元素范围很大，不能利用直接寻址表，
所以通过多次划分，逐步确定范围，然后最后在一个可以接受的范围内进行。

密匙三：Bloom filter/Bitmap

密匙四、Trie树/数据库/倒排索引 

密匙五、外排序
"""



# https://blog.csdn.net/luanpeng825485697/article/details/79974835
# https://blog.csdn.net/cbjcry/article/details/84917432
# https://blog.csdn.net/qq1404510094/article/details/80323168
