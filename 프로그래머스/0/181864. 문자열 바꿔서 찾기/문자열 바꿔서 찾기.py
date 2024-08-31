# My Code
def solution(myString, pat):
    temp_string = ''.join(["A" if string == "B" else "B" for string in myString])
    answer = 1 if pat in temp_string else 0                
    return answer