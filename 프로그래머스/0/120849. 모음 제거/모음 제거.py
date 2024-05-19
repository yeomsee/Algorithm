def solution(my_string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for string in my_string:
        if string not in vowel_list:
            answer += string
    return answer