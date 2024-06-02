# My Code
def solution(age):
    age = str(age)
    answer = ''.join([chr(ord('a') + int(num)) for num in age])
    return answer