def solution(s1, s2):
    answer = sum([1 for w1 in s1 if w1 in s2])
    return answer