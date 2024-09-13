# My Code
def solution(my_string):
    answer_list = []
    i = 0
    while i < len(my_string):
        if my_string[i] == 'a' or my_string[i] == 'b' or my_string[i] == 'c':
            temp_string = my_string[:i]
            if temp_string != "":
                answer_list.append(temp_string)
            my_string = my_string[i+1:]
            i = 0 # return to first index
        else:
            i += 1 
    if my_string != "":
        answer_list.append(my_string)
        
    if len(answer_list) == 0:
        answer_list = ["EMPTY"]
        
    return answer_list

# Best Code
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']

'''
    이외에도 정규표현식을 이용한 방법도 있는데,,,
    정규표현식 특성상 시간복잡도가 높아서 이용해도 되는지 물어보고 써야할 듯 ㅇㅇ,,
'''
