class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in parentheses:
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop() # pop unmatching val
            else:
                stack.append(char)
        return len(stack) == 0