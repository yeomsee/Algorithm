# My Code
def solution(my_string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for string in my_string:
        if string not in vowel_list:
            answer += string
    return answer

# Best Code(Simpler Ver.)
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

'''
    사실 시간 복잡도 측면에서는 차이가 없을 듯..
'''

# Another Code
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
