# My Code
def solution(phone_number):
    answer_string = ''
    for i in range(len(phone_number)-4):
        answer_string += '*'
    answer_string += phone_number[-4:]
    return answer_string

# Best Code
def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]
