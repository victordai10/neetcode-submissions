class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # pass to get the difference in a hashmap, check for val to add to get target
        numMap = {}
        for i, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = i
            diff = target - num
            if diff in numMap and numMap[diff] != i:
                return [numMap[diff], i]
        return [0, 0]



