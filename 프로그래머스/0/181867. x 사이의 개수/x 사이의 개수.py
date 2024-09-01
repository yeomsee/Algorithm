# My Code
def solution(myString):
    temp_list = myString.split("x")
    answer = [len(temp) for temp in temp_list]
    return answer