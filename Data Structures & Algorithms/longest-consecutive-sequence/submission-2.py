class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        union_find = UnionFind(nums)

        for num in nums:
            if num + 1 in union_find.parent:
                union_find.union(num, num + 1)
        
        return union_find.max_size

class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}
        self.max_size = 1

    def find_parent(self, num):
        if self.parent[num] == num:
            return num
        return self.find_parent(self.parent[num])

    def union(self, x, y):
        x_root = self.find_parent(x)
        y_root = self.find_parent(y)

        if x_root == y_root:
            return

        if self.size[x_root] <= self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
            self.max_size = max(self.max_size, self.size[y_root])

        if self.size[x_root] > self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.max_size = max(self.max_size, self.size[x_root])

        
