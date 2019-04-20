def twoSum(nums, target):
    d = {}
    for x in range(len(nums)):
        a = target - nums[x]
        if nums[x] in d:
            return d[nums[x]], x
        else:
            d[a] = x
            
L = [1,2,3,4,5,6]
func(L, 9)
