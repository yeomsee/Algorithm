# My Code
def solution(dots):
    x_list, y_list = [], []
    for x, y in dots:
        x_list.append(x), y_list.append(y)
    x_m, x_M, y_m, y_M = min(x_list), max(x_list), min(y_list), max(y_list)
    
    return (x_M - x_m)*(y_M - y_m)

# Best Code ... 수학적으로 생각해보기
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
