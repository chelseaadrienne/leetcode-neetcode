class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start, segments, path):
            # segments = each section that needs a dot
            # this is also the base case of the problem
            if segments == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            # numbers outside of the base case
            for length in range(1, 4):
                # out of range check
                if start + length > len(s):
                    break
                segment = s[start: start + length] # grabs the appropiate length of characters
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                path.append(segment)
                backtrack(start + length, segments + 1, path) # recursive call
                path.pop() # backtrack
        backtrack(0, 0, [])
        return res