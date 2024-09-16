# My Code
def solution(pictures, k):
    answer = []
    for picture in pictures:
        for _ in range(k):
            temp_string = ''.join([picture[i]*k for i in range(len(picture))])
            answer.append(temp_string)
    
    return answer

# Best Code
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer

'''
    replace를 적극적으로 쓰지 못 하는 거 같다,,!
'''
