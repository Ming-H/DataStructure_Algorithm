"""
最长回文串问题
基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的
部分的最长回文子串加上头和尾。如果头和尾不同，那么它的最长回文子串是去头的部分的
最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
P[i,j]表示第i到第j个字符的回文子串数 
dp[i,i]=1 
dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j] 
dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]
"""


def longestPalindrome(s):
    maxl = 0
    start = 0
    for i in range(len(s)):
        if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
            start = i - maxl
            maxl += 1
    return s[start: start + maxl]
    
    
# 参考文献：https://blog.csdn.net/asd136912/article/details/78987624
