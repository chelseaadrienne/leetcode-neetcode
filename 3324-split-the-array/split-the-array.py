from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for frequency in count.values():
            if frequency > 2:
                return False
        return True