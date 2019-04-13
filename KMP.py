def match_kmp(t,p,pnext):
    ''' KMP串匹配，主函数 '''
    j , i = 0 , 0
    n , m = len(t) , len(p)
    while j < n and i < m:               # i == m 说明找到匹配
        if i == -1 or t[j] == p[i] :     # 遇到 -1 ，比较下一个字符
            j , i = j + 1 , i + 1
        else :
            i = pnext[i]                 # 从pnext中取得p的下个字符的位置
    if i == m :     # 匹配成功，返回其下标
        print(j-i)
        return j - i
    print("No")
    return -1                            # 匹配失败，返回特殊值
    
def gen_pnext(p):
    ''' 生成针对指针p中各位置i的下一个检查的位置表，用于KMP算法 '''
    i , k , m = 0, -1 ,len(p)        # k 即 pnext 表中的值
    pnext = [-1] * m                 # 初始化 pnext 表
    while i < m - 1:
        if k == -1 or p[i] == p[k]:   # k = -1 代表 最长相等前后缀长度是0
            i , k = i + 1 , k + 1
            pnext[i] = k             # 设置pnext元素
            if p[i] == p[k]:           # 这里进行了优化 
                pnext[i] = pnext[k]
        else :
            k = pnext[k]             # 遇到更短相同前缀
    return pnext
            
if __name__ == "__main__":
    T = "BBC ABCDAB ABCDABCDABDE"
    P = "ABCDABCD"
    pnext = gen_pnext(P)
    print(pnext)
    match_kmp(T,P,pnext)
            

参考文献：https://www.cnblogs.com/zlsgh/p/9537793.html
注：原文代码有误
            
            
            
            
            
            
            
            
            
            
    
