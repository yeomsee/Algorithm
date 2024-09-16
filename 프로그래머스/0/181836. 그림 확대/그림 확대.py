# My Code
def solution(pictures, k):
    answer = []
    for picture in pictures:
        for _ in range(k):
            temp_string = ''.join([picture[i]*k for i in range(len(picture))])
            answer.append(temp_string)
    
    return answer