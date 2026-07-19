class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        longest = 0
        max_f = 0

        if n <= 1:
            return n

        counter = {}

        for right in range(n):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            max_f = max(max_f, counter[s[right]])

            while (right - left + 1) - max_f > k:
                if counter[s[left]] >= 1:
                    counter[s[left]] -= 1
                else:
                    del counter[s[left]]
                
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest
