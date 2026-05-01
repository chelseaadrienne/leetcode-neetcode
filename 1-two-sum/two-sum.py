class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # hashmap (dict)
        for i in range(len(nums)):
            visited[nums[i]] = i
        for i in range(len(nums)):
            match = target - nums[i] # num we need to get to add up target
            if match in visited and visited[match] != i: # check hp if num is in there & make sure we are not repeating indices
                return [i, visited[match]] # returns index, and value stored at key
        return [] # no answer available