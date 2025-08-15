class TwoSum(object):
    def twoSum(self, nums, target):
        emptyArray = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in emptyArray:
                return [emptyArray[x], i]
            emptyArray[num] = i
        return []
    # o(n) complexity solution