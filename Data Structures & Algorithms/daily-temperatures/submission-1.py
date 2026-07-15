class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        idx = n - 1

        while idx >= 0:
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                res[idx] = stack[-1] - idx

            stack.append(idx)
            idx -= 1

        return res