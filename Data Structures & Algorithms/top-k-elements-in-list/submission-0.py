import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

    # Step 3: Extract top k elements
        top_k = [item[0] for item in sorted_dic[:k]]

        return top_k
