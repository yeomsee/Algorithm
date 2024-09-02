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