# My Code
def solution(my_string):
    answer = ''
    for string in my_string:
        if (string.isdigit()): # isdigit() 적극적으로 활용자
            answer += string
        else:
            answer += ' '
    
    sum = 0
    for num in answer.split():
        sum += int(num)
    return sum