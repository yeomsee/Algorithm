# My Code
def solution(myString):
    answer = [string for string in myString.split("x") if string != ""]
    answer.sort()
    
    return answer

# Simpler Code
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)

'''
    if ch이면 공백인 문자는 제거할 수 있음

    그리고 sorted의 경우는 애초에 반환이 리스트인 점 기억!
'''
