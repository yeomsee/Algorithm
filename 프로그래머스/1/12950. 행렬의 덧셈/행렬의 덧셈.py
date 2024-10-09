# My Code
def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        temp_list = [x[i]+y[i] for i in range(len(x))]
        answer.append(temp_list)
        
    return answer

# Best Code
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

'''
    사실 이렇게 구현하고 싶었던 거였음 ㅎㅎ,,
'''
