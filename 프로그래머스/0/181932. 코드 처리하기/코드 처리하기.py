# My Code
def solution(code):
    mode, ret = 0, ''
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = (mode+1)%2
        elif (mode == 0 and idx%2 == 0) or (mode == 1 and idx%2 != 0):
            ret += code[idx]

    if len(ret) == 0:
        return "EMPTY"
    return ret