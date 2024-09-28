# My Code
def solution(num, total):
    if num%2 != 0:
        mid = total//num
        start, end = mid - (num-1)//2, mid + (num-1)//2
        return [x for x in range(start, end+1)]
    else:
        mid_l, mid_r = total//num, total//num + 1
        start, end = mid_l - num//2 + 1, mid_r + num//2 - 1
        return [x for x in range(start, end+1)]        