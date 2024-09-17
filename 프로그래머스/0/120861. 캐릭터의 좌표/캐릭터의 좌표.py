# My Code
def solution(keyinput, board):
    x_half, y_half = board[0]//2, board[1]//2
    answer = [0, 0]
    
    for key in keyinput:
        if key == "left":
            answer[0] -= 1
            if answer[0] < -x_half:
                answer[0] = -x_half
        elif key == "right":
            answer[0] += 1
            if answer[0] > x_half:
                answer[0] = x_half
        elif key == "up":
            answer[1] += 1
            if answer[1] > y_half:
                answer[1] = y_half
        elif key == "down":
            answer[1] -= 1
            if answer[1] < -y_half:
                answer[1] = -y_half

    return answer

# Simpler Code
def solution(keyinput, board):
    curr = [0, 0]
    for k in keyinput:
        if k == 'left':
            curr[0] = max(curr[0] - 1, -(board[0] // 2))
        elif k == 'right':
            curr[0] = min(curr[0] + 1, board[0] // 2)
        elif k == 'down':
            curr[1] = max(curr[1] - 1, -(board[1] // 2))
        else:
            curr[1] = min(curr[1] + 1, board[1] // 2)

    return curr
