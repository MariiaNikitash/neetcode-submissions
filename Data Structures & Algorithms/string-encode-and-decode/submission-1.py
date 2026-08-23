class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        def length(w):
            length_w = len(w)
            res = str(length_w) + '#' + w
            return res
        
        for word in strs:
            result.append(length(word))
        return ''.join(result)
        #4#love#8neetcode
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1 # increment till #
            # convert digit to a int so we can fast forward for that many letters
            length = int(s[i:j]) # so for xample '4#love - len is 4 
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length # shift i to next 
        return res