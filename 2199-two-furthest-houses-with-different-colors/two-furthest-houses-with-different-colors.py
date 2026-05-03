class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)

        for i in range(n):
            if colors[i] != colors[0]: # check against first house
                res = max(res, i)
            if colors[i] != colors[n-1]: # check against the last house
                res = max(res, n - 1 - i)
        return res