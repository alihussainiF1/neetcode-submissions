class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW,COL=len(board),len(board[0])
        row_dict,col_dict,square_dict={},{},{}

        for i in range(9):
            row_dict[i],col_dict[i]=set(),set()
        for i in range(9):
            for j in range(9):
                square_dict[(i//3,j//3)]=set()

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                else:
                    val=board[r][c]
                    if val not in row_dict[r] and val not in col_dict[c] and val not in square_dict[(r//3,c//3)]:
                        row_dict[r].add(val)
                        col_dict[c].add(val)
                        square_dict[(r//3,c//3)].add(val)
                    else:
                        return False
        return True