import re
#import string

class Solution(object):
    def isPalindrome(self, s):
        concat_string = re.sub(r"[^A-Za-z0-9]", "", s).lower() # removes anything that is not a letter or number & makes it lowercase
        reversed_concat_string = concat_string[::-1] # reverses tring
        return concat_string == reversed_concat_string
        