from typing import List
from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.points_dict = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.points_dict[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        qx, qy = point
        for x, y in self.points:
            # check for diagonal values which are perpendicular
            if (abs(qx - x) != abs(qy - y)) or x == qx or y == qy:
                continue
            result += self.points_dict[(x, qy)] * self.points_dict[(qx, y)]

        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
