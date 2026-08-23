class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        prefix = []
        word1 = strs[0]
        for index in range(len(word1)):
            ch = word1[index]
            for word in strs:
                if index >= len(word) or ch != word[index]:
                    return ''.join(prefix)
            prefix.append(ch)
        
        return ''.join(prefix)

        
            


        
