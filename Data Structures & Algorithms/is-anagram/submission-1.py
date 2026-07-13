class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for c in s:
            if c not in s_count:
                s_count[c] = 1
            else:
                s_count[c] += 1

        for c in t:
            if c not in t_count:
                t_count[c] = 1
            else:
                t_count[c] += 1

        for key, val in s_count.items():
            if key not in t_count:
                return False
            if s_count[key] != t_count[key]:
                return False
        
        for key, val in t_count.items():
            if key not in s_count:
                return False
            if s_count[key] != t_count[key]:
                return False
        
        return True