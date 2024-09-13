# My Code
def solution(arr):
    x = 0
    while True:
        new_arr = []
        for num in arr:
            if num >= 50 and num%2 == 0:
                new_arr.append(num/2)
            elif num < 50 and num%2 != 0:
                new_arr.append(num*2 + 1)
            else:
                new_arr.append(num)

        if new_arr == arr:
            return x
        x += 1
        arr = new_arr
        
    return answer