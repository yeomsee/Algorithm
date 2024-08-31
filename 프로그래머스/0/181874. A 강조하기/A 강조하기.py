# My Code
def solution(myString):
    answer = ''
    for string in myString:
        if string == 'a':
            answer += 'A'
        elif string.isupper() and string != 'A':
            answer += string.lower()
        else:
            answer += string
            
    return answer

# Best Code
def solution(myString):
    return myString.lower().replace('a', 'A')
