class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        valid=True
        for i in range(9):
            for j in range(9):
                number=board[i][j]
                if number == ".":
                    continue
                if number in row[i]:
                    valid = False
                row[i].add(number)
                if number in col[j]:
                    valid=False
                col[j].add(number)
                
                box = (i//3)*3 + (j//3)
                if number in boxes[box]:
                    valid = False
                boxes[box].add(number)  
        return valid
                