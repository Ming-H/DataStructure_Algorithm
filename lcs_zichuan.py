# -*- codind:utf-8 -*-

def lcs(str_a, str_b):
    if len(str_a) ==0 or len(str_b) == 0:
        return 0
    dp = [[0 for _ in range(len(str_b)+1)] for _ in range(len(str_a)+1)]
    max_len = 0
    lcs_str = ""
    for i in range(1, len(str_a)+1):
        for j in range(1, len(str_b)+1):
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
                if max_len == dp[i][j]:
                    lcs_str = str_a[i-max_len:i]
            else:
              dp[i][j] = 0
    print("length of LCS is :",max_len)
    print("LCS :",lcs_str)


def space_efficient_lcs(str_a, str_b):
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
    print(lcs_str)


'''
求两个字符串的最长公共子串
思想：建立一个二维数组，保存连续位相同与否的状态
'''
 
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]  # 多一位
    maxNum = 0          # 最长匹配长度
    p = 0               # 匹配的起始位
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i+1][j+1] = record[i][j] + 1
                if record[i+1][j+1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i+1][j+1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p-maxNum:p], maxNum



if __name__ == '__main__':
    a='ABCBDABbbb'
    b='BDCABABbbb'
    res = getNumofCommonSubstr(a,b)
    print(res)

    b='BDCABABbbb'
    lcs(a, b)
    space_efficient_lcs(a,b)


