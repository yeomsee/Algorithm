# My Code
def solution(slice, n):
    answer = n // slice if n % slice == 0 else n // slice + 1
    return answer

# Best Code : Simpler Ver.
def solution(slice, n):
    return ((n - 1) // slice) + 1

'''
    지난 번에도 봤던 코드인 거 같은데 아직 익숙해지지 않았다ㅠㅠ
'''
