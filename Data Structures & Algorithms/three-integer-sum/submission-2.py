class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            num = nums[i]
            left = i + 1
            right = n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1

        return res