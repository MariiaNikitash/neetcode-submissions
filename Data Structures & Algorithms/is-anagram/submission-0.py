class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for i in s:
            if i not in dicS:
                dicS[i] = 1
            else: 
                dicS[i] += 1

        for i in t:
            if i not in dicT:
                dicT[i] = 1
            else: 
                dicT[i] += 1
        return dicS == dicT