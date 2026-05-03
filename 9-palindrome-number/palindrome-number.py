class Solution:
    def isPalindrome(self, x: int) -> bool:
        numToString = str(x) # convert from int to string
        reversedString = numToString[::-1] # reverse order of string
        if (numToString == reversedString): # check for equality
            return True
        return False