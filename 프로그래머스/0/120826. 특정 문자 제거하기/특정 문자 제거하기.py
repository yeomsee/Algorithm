# My Code = Best Code
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer

# Another Code1 : replace 사용 X
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer

'''
    원래는 이걸로 하려고했지만 좀 더 간결하고 직관적인 코드를 작성하고 싶었음!
'''

# Another Code2 : join 활용
def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])
