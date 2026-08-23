class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        track length of longest substring
        
        i will need a left and rig=ght pointer 
        a count to track thelongest
        i iterate over '''
        
        if not s:
            return 0
        res = 0
        l = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r-l + 1)
            
        return res
            
        
