class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]

        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for c in s:
            if c in opening:
                stack.append(c)
            if c in closing:
                if not stack:
                    return False
                open = stack.pop()
                if match[c] != open:
                    return False
        
        return not stack