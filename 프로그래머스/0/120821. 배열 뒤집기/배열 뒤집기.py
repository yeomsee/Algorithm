# My Code
def solution(num_list):
    num_list.reverse()
    
    return num_list

'''
    reverse는 반환값이 없음. 기존의 배열을 뒤집기 때문에 복원 불가능하다는 단점.
'''

# My Code2
def solution(num_list):
    answer = list(reversed(num_list))

    return answer

'''
    반환값이 iterator. 때문에 list() 함수를 이용하여 iterator를 반환해야함.
'''

# Another Code
def solution(num_list):
    return num_list[::-1]

'''
    하지만, 이 방법은 메모리 사용량이 많다는 단점이 있음.
'''
