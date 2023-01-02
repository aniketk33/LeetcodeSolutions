'''There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 1:
            return False
        left_right_val = 0
        up_down_val = 0
        for move in moves:
            if move in ['U', 'D']:
                up_down_val += -1 if move == 'D' else 1
            else:
                left_right_val += -1 if move == 'L' else 1
        
        return (left_right_val == 0 and up_down_val == 0)

moves = "UD"
soln = Solution().judgeCircle(moves)
print(soln)
            