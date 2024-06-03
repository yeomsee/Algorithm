# My Code
def solution(my_string):
    answer = []
    for string in my_string:
        if string >= "0" and string <= "9":
            answer.append(int(string))
    answer.sort()
    return answer