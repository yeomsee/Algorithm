# My Code
def solution(phone_number):
    answer_string = ''
    for i in range(len(phone_number)-4):
        answer_string += '*'
    answer_string += phone_number[-4:]
    return answer_string