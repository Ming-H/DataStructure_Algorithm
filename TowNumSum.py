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


def combinationSum2(candidates, target):
    """
    和为定值的组合，每个值只能用一次
    """
    candidates.sort()                      
    result = []
    combine_sum_2(candidates, 0, [], result, target)
    return result
    
def combine_sum_2(nums, start, path, result, target):
    if not target:
        result.append(path)
        return
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        if nums[i] > target:
            break
        combine_sum_2(nums, i + 1, path + [nums[i]], 
                        result, target - nums[i])

candidates = [2,5,2,1,2]
target = 5
print(combinationSum2(candidates, target))
