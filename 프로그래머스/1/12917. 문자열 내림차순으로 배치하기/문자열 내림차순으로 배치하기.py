# My Code
def solution(string):
    string_list = sorted([s for s in string], key = lambda x : ord(x), reverse=True)
    return ''.join(string_list)