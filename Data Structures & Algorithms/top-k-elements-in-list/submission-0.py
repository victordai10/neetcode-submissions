class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap key = num, value = frequency
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # first pass to collect the frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # second pass, update freq array, where index = frequency, and value is num
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            



