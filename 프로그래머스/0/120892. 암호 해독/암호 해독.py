# My Code
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
        
    return answer

# Best Code(Simpler Ver.)
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

'''
    list slicing에 대한 이해가 부족했던 듯,,
    좀 더 간단하고 직관적이게 짜보려고 노력하자!
'''
