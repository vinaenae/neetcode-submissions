class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            curr_row_counter = [] #o1
            curr_column_counter = [] # o1
            for r in range(len(board[i])): #on
                if board[i][r] != ".":
                    if board[i][r] in curr_row_counter: #O(n)
                        return False
                    curr_row_counter.append(board[i][r])
                if board[r][i] != ".": #o1
                    if board[r][i] in curr_column_counter: #on              
                        return False
                    curr_column_counter.append(board[r][i]) #o1
                

        for i in range(0, 9, 3): #on
                for j in range(0, 9, 3): #on
                    box_counter = [] #o1
                    for c in range(i,i+3): #o3 - o1
                        for d in range(j,j+3): #o3 - o1
                            if board[c][d] != ".": #o1
                                if board[c][d] in box_counter: #on
                                    return False
                                box_counter.append(board[c][d]) #o1
        return True
            







        