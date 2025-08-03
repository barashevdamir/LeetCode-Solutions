class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mapping ={
            "R": 1,
            "L": -1,
            "U": 1,
            "D": -1
        }
        y_move = ["U", "D"]
        curr_pos_x = 0
        curr_pos_y = 0
        for move in moves:
            if move in y_move:
                curr_pos_y += mapping[move]
            else:
                curr_pos_x += mapping[move]
        
        return (curr_pos_y == 0) and (curr_pos_x == 0)

