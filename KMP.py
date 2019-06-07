#-*- coding:utf-8 -*-

def match_kmp(t, p, pnext):
    ''' KMP串匹配，主函数 '''
    i = 0
    j = 0
    m = len(t)
    n = len(p)
    while i<m and j<n:                  # j == n 说明找到匹配
        if j==-1 or t[i]==p[j]:         # 遇到 -1 ，比较下一个字符
            i, j = i+1, j+1             
        else:                           
            j = pnext[j]                # 从pnext中取得p的下个字符的位置
    if j==n:                            
        print(i-j)                      
        return i-j                      
    return -1                           
                                        
def gen_pnext(p):   
    ''' 生成针对指针p中各位置i的下一个检查的位置表，用于KMP算法 '''
    i, k = 0, -1                        # k 即 pnext 表中的值
    pnext = [-1 for i in range(len(p))] # 初始化 pnext 表
    while i<len(p)-1:
        if k==-1 or p[i]==p[k]:         # k = -1 代表 最长相等前后缀长度是0
            i,k = i+1,k+1
            pnext[i] = k                # 设置pnext元素
            if p[i] == p[k]:            # 这里进行了优化 
                pnext[i] = pnext[k]
        else:
            k = pnext[k]                # 遇到更短相同前缀
    return pnext
    
def strStr(T, P):
    if P == "":
        return 0
    for i in range(len(T)-len(P)+1):
        for j in range(len(P)):
            if T[i+j] != P[j]:
                break
            if j == len(P)-1:
                return i
    return -1


    
if __name__ == "__main__":
    T = "BBC ABCDAB ABCDABCDABDE"
    P = "ABCDABCD"
    pnext = gen_pnext(P)
    print(pnext)
    match_kmp(T, P, pnext)
    print(strStr(T, P))


            

参考文献：https://www.cnblogs.com/zlsgh/p/9537793.html
　kmp 算法的时间复杂度是 O(m+n)
注：原文代码有误
            
            
            
            
            
            
            
            
            
            
    
