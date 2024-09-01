# My Code
def solution(n):
    if n%2 != 0:
        temp_list = [x for x in range(1, n+1) if x%2 != 0]
        return sum(temp_list)
    else:
        temp_list = [x**2 for x in range(1, n+1) if x%2 == 0]
        return sum(temp_list)