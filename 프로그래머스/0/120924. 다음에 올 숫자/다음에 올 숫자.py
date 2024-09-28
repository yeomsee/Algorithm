# My Code
def solution(common):
    if (common[1] - common[0]) == (common[2] - common[1]):
        return common[-1] + (common[1] - common[0])
    else: # 등비수열의 경우
        return common[-1] * (common[1] // common[0])
    
    return answer