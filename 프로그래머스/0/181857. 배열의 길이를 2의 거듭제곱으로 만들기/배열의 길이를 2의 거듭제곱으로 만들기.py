# My Code
def solution(arr):
    i = 0
    while True:
        if len(arr) == 2**i:
            return arr
        elif len(arr) > 2**i:
            i += 1
        else: # len(arr) < 2**i
            surplus = 2**i - len(arr)
            arr.extend([0]*surplus)
            return arr

# Simpler Code
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)
'''
    논리는 비슷한데 훨씬 더 직관적이고 효율적인 코딩이라고 생각해서 들고왔습니다.
'''
