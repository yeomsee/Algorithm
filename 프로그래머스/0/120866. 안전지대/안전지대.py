# My Code
def solution(board):
    danger_list = []
    lookup_list = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    
    # board index를 넘어가는지 check하는 함수
    def check_access(i, j, row_num, col_num):
        if 0 <= i < col_num and 0<= j < row_num:
            return True
        return False
    
    row_num, col_num = len(board), len(board[0])
    for i in range(row_num):
        for j in range(col_num):
            if board[i][j] == 1:
                for i_look, j_look in lookup_list:
                    if check_access(i+i_look, j+j_look, row_num, col_num) and [i+i_look, j+j_look] not in danger_list:
                        danger_list.append([i+i_look, j+j_look])
                    if [i, j] not in danger_list:
                        danger_list.append([i, j])
                
                
    return (row_num)*(col_num) - len(danger_list)