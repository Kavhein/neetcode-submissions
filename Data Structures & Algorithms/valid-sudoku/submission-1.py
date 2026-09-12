class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            seen=set()
            for j in range(0,9):
                number = board[i][j]
                if number == ".":
                    continue
                if number in seen:
                    return False
                else:
                    seen.add(number)
        for i in range(0,9):
            seen=set()
            for j in range(0,9):
                number = board[j][i]
                if number == ".":
                    continue
                if number in seen:
                    return False
                else:
                    seen.add(number)
        for box in range(9):
            seen = set()
            rows = (box // 3) * 3
            cols = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    print(rows,cols)
                    number = board[rows+i][cols+j]
                    if number == ".":
                        continue
                    if number in seen:
                        return False
                    else:
                        seen.add(number)
        return True
                