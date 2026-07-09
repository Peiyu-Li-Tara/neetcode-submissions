class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or not self.map[key]:
            return ""

        # # brute force
        # ret = ""
        # for time, val in self.map[key]:
        #     if time > timestamp:
        #         return ret
        #     ret = val
        # return ret

        # binary search
        ret = ""
        values = self.map[key] 
        start, end = 0, len(values) - 1
        while start <= end:
            mid = (start + end) // 2
            if values[mid][1] <= timestamp:
                ret = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return ret
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
