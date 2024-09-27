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

# Best Code
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'

'''
    많이 쓰일 것 같지는 않지만,, '^=' 연산자에 대하여,,
    ^=은 xor을 뜻함
    두 비트가 서로 같다면 0을 서로 다르다면 1을 return
'''
