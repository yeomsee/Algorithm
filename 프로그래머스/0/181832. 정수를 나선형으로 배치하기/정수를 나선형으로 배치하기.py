# My Code
def solution(n):
    # initialize
    answer = [[0 for j in range(n)] for i in range(n)]
    
    x, y = 0, 0
    mode = 0
    for i in range(n*n):
        answer[x][y] = i+1
        if mode%4 == 0:        
            if (y == n-1) or (answer[x][y+1] != 0):
                mode += 1
                x += 1
            else:
                y += 1
        elif mode%4 == 1:
            if x == n-1 or (answer[x+1][y] != 0):
                mode += 1
                y -= 1
            else:
                x += 1
        elif mode%4 == 2:
            if x == 0 or (answer[x][y-1] != 0):
                mode += 1
                x -= 1
            else:
                y -= 1
        else: # mode%4 == 3
            if answer[x-1][y] != 0:
                mode += 1
                y += 1
            else:
                x -= 1

    return answer