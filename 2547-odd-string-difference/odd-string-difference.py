class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(word):
            # return list of differences in words
            # ord() converts char to ASCII
            return [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]
        
        seen = {}
        # loop through and compute its difference pattern
        for word in words:
            difference = tuple(diff(word))
            # if unseen pattern difference then store in dict
            if difference not in seen:
                seen[difference] = word
            else:
                seen[difference] = None
        
        # whatever that wasn't marked as None has the unique pattern difference
        for difference, word in seen.items():
            if word is not None:
                return word