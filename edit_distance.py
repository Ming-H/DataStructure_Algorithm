
"""
最小编辑距离或莱文斯坦距离（Levenshtein），
指由字符串A转化为字符串B的最小编辑次数。
允许的编辑操作有：删除，插入，替换
"""

def normal_leven(str1, str2):
      len_str1 = len(str1) + 1
      len_str2 = len(str2) + 1
      matrix = [0 for n in range(len_str1 * len_str2)]
      for i in range(len_str1):
          matrix[i] = i
      for j in range(0, len(matrix), len_str1):
          if j % len_str1 == 0:
              matrix[j] = j // len_str1
          
      for i in range(1, len_str1):
          for j in range(1, len_str2):
              if str1[i-1] == str2[j-1]:
                  cost = 0
              else:
                  cost = 1
              matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                                          matrix[j*len_str1+(i-1)]+1,
                                          matrix[(j-1)*len_str1+(i-1)] + cost)
          
      return matrix[-1]
      

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
 
 
print(edit('ofailing','osailn'))
print(normal_leven('ofailing','osailn'))

# 参考文献：https://www.jianshu.com/p/466cf6624e26
# https://blog.csdn.net/u010897775/article/details/40018889
