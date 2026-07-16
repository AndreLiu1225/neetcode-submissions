class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        lst = self.timemap[key]
        left = 0
        right = len(lst) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if lst[mid][1] <= timestamp:
                left = mid + 1
                res = lst[mid][0]
            else:
                right = mid - 1
        
        return res
