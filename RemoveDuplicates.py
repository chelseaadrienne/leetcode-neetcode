class Solution:
    def RemoveDuplicates(self, nums: List[int]) -> int:
        c = 0
        number = len(nums)
        for i in range(1, number):
            if (nums[i] == nums[i-1]):
                c += 1
            else:
                nums[i-c] = nums[i]
        return(number-c)