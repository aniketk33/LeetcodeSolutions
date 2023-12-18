class TimeMap:

    def __init__(self):
        # dict to store the key and list of [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        left_ptr, right_ptr = 0, len(values) - 1

        while left_ptr <= right_ptr:
            mid_idx = left_ptr + (right_ptr - left_ptr) // 2
            if values[mid_idx][1] == timestamp:
                return values[mid_idx][0]
            if values[mid_idx][1] < timestamp:
                # return the value for given timestamp
                result = values[mid_idx][0]
                left_ptr = mid_idx + 1
            else:
                right_ptr = mid_idx - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
