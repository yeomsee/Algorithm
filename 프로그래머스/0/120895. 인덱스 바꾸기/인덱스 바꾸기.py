# My Code
def solution(my_string, num1, num2):
    answer = ''

    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer

# Best Code
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

'''
    Eg.
    my_string = 'python'
    list(my_string) = ['p', 'y', 't', 'h', 'o', 'n']
    
    처음에는 my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    But, 'str' object does not support item assignment
    때문에 위처럼 리스트로 바꿔서 실행
'''
