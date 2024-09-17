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