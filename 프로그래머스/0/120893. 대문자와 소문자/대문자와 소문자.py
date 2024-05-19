def solution(my_string):
    answer = ''
    for string in my_string:
        if 'a' <= string <= 'z':
            answer += string.upper()
        elif 'A' <= string <= 'Z':
            answer += string.lower()
    
    return answer