# 在第i个元素时，我们能够取到的子序列的最大乘积可能来自：
# （1）nums[i]本身
# （2）nums[i-1]能够取到的最大子序列的乘积
# （3）包含nums[i-1]的最大连乘值 * nums[i] (两个部分均为正数)
# （4）包含nums[i-1]的最小连乘值 * nums[i] (两个部分均为负数)
# 因此对于第i个元素，我们需要记录的值有三个：
# （1）能够取到的子序列的最大乘积
# （2）包含当前位置的最大连乘值
# （3）包含当前位置的最小连乘值

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #temp记录整个数组的子序列最大连乘积
    temp = nums[0]
    length = len(nums)
    
    #M数组记录包含当前位置的最大连乘值
    M = [0 for i in range(length)]
    #m数组记录包含当前位置的最小连乘值
    m = [0 for i in range(length)]
    
    for i in range(length):
        if i == 0:
            M[i] = nums[i]
            m[i] = nums[i]
        else:
            #包含当前位置的最大连乘值从：当前位置和到第i-1个元素的最大连乘值的乘积、当前元素中选出
            M[i] = max(max(M[i-1]*nums[i], m[i-1]*nums[i]), nums[i])
            m[i] = min(min(M[i-1]*nums[i], m[i-1]*nums[i]), nums[i])
            
        temp = max(temp,M[i])
        
    return temp

if __name__ == "__main__":
    nums = [-2,0,-1,-3,6]
    print(maxProduct(nums))
