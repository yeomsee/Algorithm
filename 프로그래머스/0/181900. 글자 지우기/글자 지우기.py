# My Code
def solution(my_string, indices):
    return ''.join([my_string[idx] for idx in range(len(my_string)) if idx not in indices])