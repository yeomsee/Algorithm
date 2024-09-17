# My Code
def solution(M, N):
    if M==0 and N==0:
        return 0
    return (M-1) + M*(N-1)