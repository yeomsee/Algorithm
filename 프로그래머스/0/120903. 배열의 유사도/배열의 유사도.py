# My Code
def solution(s1, s2):
    answer = sum([1 for w1 in s1 if w1 in s2])
    return answer

# Best Code : set을 이용한 효율적인 처리
def solution(s1, s2):
    return len(set(s1)&set(s2))
