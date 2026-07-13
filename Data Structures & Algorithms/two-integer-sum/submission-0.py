class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in needed:
                return [needed[num], i]
            
            leftover = target - num
            needed[leftover] = i
        
