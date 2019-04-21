def towSum(L, target):
    """
    两数之和为定值
    """
    d = {}
    for i in range(len(L)):
        if L[i] not in d:
            d[target - L[i]] = i 
        else:
            return d[L[i]], i
            
L = [1,3,5,6]
print(towSum(L, 7))


def twosum(nums, target):
    nums.sort()
    result = []
    sum_method(nums, 0, [], result, target)
    return result
    
def sum_method(nums, start, path, result, target):
    if not target:
        result.append(path)
        return 
    for i in range(start, len(nums)):
        if i>start and nums[i]==nums[i-1]:
            continue
        if nums[i]>target:
            break
        sum_method(nums, start+1, path+[nums[i]], result, target-nums[i])

candidates = [2,5,2,1,2]
target = 5
print(twosum(candidates, target))
