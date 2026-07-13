class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_list_string = defaultdict(list)

        for s in strs:
            alphabets = [0] * 26
            for c in s:
                alphabets[ord(c) - ord('a')] += 1
            
            letter_list_string[tuple(alphabets)].append(s)
            
        res = []
        for val in letter_list_string.values():
            res.append(val)
        return res