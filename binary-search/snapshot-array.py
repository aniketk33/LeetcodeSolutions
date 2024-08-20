class SnapshotArray:

    def __init__(self, length: int):
        # creating a history array with snap ids and value for every index
        self.histories = []
        self.snap_id = 0
        for _ in range(length):
            self.histories.append([[-1, 0]])

    def set(self, index: int, val: int) -> None:
        # set the current snap and the value for the given index
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.histories[index]) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            # we have to store the latest value for the given snap id, so moving the left pointer towards the latest
            # value
            if self.histories[index][mid][0] <= snap_id:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return self.histories[index][result][1]

    # Your SnapshotArray object will be instantiated and called as such:


obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
param_3 = obj.get(0, 0)
print(param_2, param_3)
