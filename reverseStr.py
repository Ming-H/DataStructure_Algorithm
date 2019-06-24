"""
字符串翻转，时间复杂度最低
"""

def reversestr(str):
    ch = list(str)
    #ch = str
    i = 0
    j = len(ch)-1
    while i<j:
        ch[i],ch[j] = ch[j],ch[i]
        i+=1
        j-=1
    return ''.join(ch)

#str = ['I', 'love', 'u']
str = "abcdefg"
print(reversestr(str))


# https://blog.csdn.net/qq_42013574/article/details/88721818
