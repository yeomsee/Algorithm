# My Code
def solution(board, k):
    temp_list = [
        board[i][j]
        for i in range(len(board))
        for j in range(len(board[i]))
        if i+j <= k
    ]
                
    return sum(temp_list)