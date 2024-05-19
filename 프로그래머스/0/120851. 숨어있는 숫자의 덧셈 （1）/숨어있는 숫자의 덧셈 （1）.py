# My Code
def solution(my_string):
    answer = sum([int(x) for x in my_string if ord("1") <= ord(x) <= ord("9")])
    return answer

# Another Code
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

'''
    str.isdigit() : str이 0 이상의 정수로만 이루어진 문자열에서만 True를 반환
'''
