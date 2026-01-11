class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()
        
        for idx in range(len(nums)):
            num = nums[idx]
            while d and d[-1] < num: # if current num is greater than last number added to deque
                d.pop() # if yes, then pop
            d.append(num) # no then add to deque
            
            if idx >= k and nums[idx - k] == d[0]: # remove the num of out of the sliding window
                d.popleft()
            
            if idx >= k - 1: # idx >= k-1 means we have a complete window, so add it to the deque
                res.append(d[0])
        return res