class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        longest = 0

        if n <= 1:
            return n

        seen.add(s[left])

        for right in range(1, n):
            while s[right] in seen:
                seen.discard(s[left])
                left += 1
                
            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest