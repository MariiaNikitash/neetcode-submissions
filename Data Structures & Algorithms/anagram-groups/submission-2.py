class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        # iterate over each str
        # check if str in # sorted str: [strs]
        for s in strs:
            srt = tuple(sorted(s))
            if srt not in dic:
                dic[srt] = [s]
            else:
                dic[srt].append(s)
        
        for v in dic.values():
            res.append(v)
        return res