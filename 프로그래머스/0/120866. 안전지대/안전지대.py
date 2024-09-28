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

# Best Code
def solution(board):
    n = len(board) # board의 row의 수
    danger = set() # 위험한 지역의 좌표를 담는 역할.. set으로 설정한 이유는 중복인 좌표는 제거하기 위해서!
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x: # board의 좌표가 0이면 폭탄이 없기 때문에 그냥 pass
                continue
            # board의 좌표가 1인 경우 danger_set에 update(set 원소 추가)
            # di, dj는 각각 i가 살펴볼 곳, j가 살펴볼 곳을 의미함
            # 때문에 board의 어떤 좌표가 1이라면 폭탄이 있기 때문에 그 주변으로 전부 다 비안전지대 -> update! 
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger) # filtering은 여기서 수행해도 괜찮음
