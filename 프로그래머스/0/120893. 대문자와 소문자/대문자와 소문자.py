# My Code
def solution(my_string):
    answer = ''
    for string in my_string:
        if 'a' <= string <= 'z':
            answer += string.upper()
        elif 'A' <= string <= 'Z':
            answer += string.lower()
    
    return answer

# Best Code
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer

'''
    str.isupper() : str의 "모든" 문자가 대문자인 경우 True를 return.
'''
