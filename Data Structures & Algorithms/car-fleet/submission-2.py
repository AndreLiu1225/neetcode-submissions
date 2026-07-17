class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            time = (target - p) / s
            
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)