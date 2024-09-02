# My Code
def solution(intStrs, k, s, l):
    return [int(num[s:s+l]) for num in intStrs if int(num[s:s+l]) > k]