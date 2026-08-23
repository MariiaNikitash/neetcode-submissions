class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        track length of longest substring
        
        i will need a left and rig=ght pointer 
        a count to track thelongest
        i iterate over '''
        
        if not s:
            return 0
        max_count = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_count = max(max_count, len(seen))
            
        return max_count
            
        
