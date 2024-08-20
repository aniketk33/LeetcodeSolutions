class SnapshotArray:

    def __init__(self, length: int):
        self.histories = []
        self.snap_count = 0
        for _ in range(length):
            # create a list of (snap_id (index), value) for each index
            self.histories.append([[-1, 0]])

    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.histories[index]) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.histories[index][mid][0] <= snap_id:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return self.histories[index][result][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
