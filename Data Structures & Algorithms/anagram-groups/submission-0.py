class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for s in strs:
            if tuple(sorted(s)) in dic:
                dic[tuple(sorted(s))].append(s)
            else:
                dic[tuple(sorted(s))] = [s]
        
        for vals in dic.values():
            ans.append(vals)
        return ans