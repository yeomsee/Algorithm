# My Code
def solution(my_string, pat):
    N = len(pat)
    for i in range(len(my_string)):
        temp_string = my_string[len(my_string)-i-N:len(my_string)-i]
        if temp_string == pat:
            return my_string[:len(my_string)-i]

# Best Code
def solution(myString, pat):
    return myString[0:myString.rfind(pat)] + pat

'''
    string.find("x") : "x"가 등장하는 위치를 왼쪽에서부터 찾음
    string.rfind("x") : "x"가 등장하는 위치를 오른쪽에서부터 찾음
'''
