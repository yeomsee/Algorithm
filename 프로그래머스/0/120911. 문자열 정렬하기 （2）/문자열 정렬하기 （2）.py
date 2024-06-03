# My Code
def solution(my_string):
    my_string = list(my_string.lower())
    my_string.sort()
    
    return ''.join(my_string)

# Another Code
def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return ''.join(sorted(answer))

'''
    한줄짜리 코드도 좋지만 이렇게 아스키 코드를 이용해서 풀줄도 알아야할 거 같다.

    영어 대문자는 65~90번까지, 소문자는 97~122번까지
'''
