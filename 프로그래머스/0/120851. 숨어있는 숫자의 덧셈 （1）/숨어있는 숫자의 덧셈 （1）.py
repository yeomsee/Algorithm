def solution(my_string):
    answer = sum([int(x) for x in my_string if ord("1") <= ord(x) <= ord("9")])
    return answer