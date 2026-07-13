class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_buckets = [[] for _ in range(n + 1)]
        frequency = defaultdict(int)

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        for num, freq in frequency.items():
            freq_buckets[freq].append(num)
        
        res = []

        for i in range(n, -1, -1):
            for num in freq_buckets[i]:
                if len(res) < k:
                    res.append(num)
        
        return res