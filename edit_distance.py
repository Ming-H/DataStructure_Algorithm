
"""
最小编辑距离或莱文斯坦距离（Levenshtein），
指由字符串A转化为字符串B的最小编辑次数。
允许的编辑操作有：删除，插入，替换
"""

def edit(str1, str2):
    matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d)
 
 
    return matrix[len(str1)][len(str2)]
 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:  
        l1, l2 = len(word1)+1, len(word2)+1
        pre = [i for i in range(l2)]
        for i in range(1, l1):
            cur = [i]*l2
            for j in range(1, l2):
                cur[j] = min(cur[j-1]+1, pre[j]+1, 
                        pre[j-1]+(word1[i-1]!=word2[j-1]))
            pre = cur[:]
        return pre[-1]


 
print(edit('ofailing','osailn'))
print(normal_leven('ofailing','osailn'))

# 参考文献：https://www.jianshu.com/p/466cf6624e26
# https://blog.csdn.net/u010897775/article/details/40018889
# https://www.cnblogs.com/zuoyuan/p/3773134.html
