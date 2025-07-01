#
# https://neetcode.io/problems/valid-sudoku?list=neetcode150
#

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row checking
        for row in range(len(board)):
            row_set = set(board[row])
            row_string = "".join(board[row])
            row_string = row_string.replace(".", "") + "."
            if len(row_set) != len(row_string):
                return False
        
        # Column checking
        for col in range(len(board)):
            col_lst = [board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col], board[6][col], board[7][col], board[8][col]]
            col_set = set(col_lst)
            col_string = "".join(col_lst)
            col_string = col_string.replace(".", "") + "."
            if len(col_set) != len(col_string):
                return False
        
        # Block checking
        ## 11, 14, 17, 41, 44, 47, 71, 74, 77
        def gather_nums(b, row, col):
            return [b[row-1][col-1], b[row-1][col], b[row-1][col+1], b[row][col-1], b[row][col], b[row][col+1], b[row+1][col-1], b[row+1][col], b[row+1][col+1]]

        block_11 = gather_nums(board, 1, 1)
        block_14 = gather_nums(board, 1, 4)
        block_17 = gather_nums(board, 1, 7)
        block_41 = gather_nums(board, 4, 1)
        block_44 = gather_nums(board, 4, 4)
        block_47 = gather_nums(board, 4, 7)
        block_71 = gather_nums(board, 7, 1)
        block_74 = gather_nums(board, 7, 4)
        block_77 = gather_nums(board, 7, 7)

        block_74 = gather_nums(board, 7, 4)
        blocks = [block_11, block_14, block_17, block_41, block_44, block_47, block_71, block_74, block_77]
        for b in blocks:
            b_lst = "".join(b)
            b_lst = b_lst.replace(".", "") + "."
            b_set = set(b)
            if len(b_lst) != len(b_set):
                return False
        
        return True
            
