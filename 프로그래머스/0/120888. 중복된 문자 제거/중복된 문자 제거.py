# My Code
def solution(my_string):
    answer_list = []
    for string in my_string:
        if len(answer_list) == 0:
            answer_list.append(string)
        else:
            if string not in answer_list:
                answer_list.append(string)
    answer = ''.join(answer_list)
    return answer