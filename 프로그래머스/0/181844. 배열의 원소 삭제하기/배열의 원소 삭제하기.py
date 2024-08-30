# My Code
def solution(arr, delete_list):
    for num2del in delete_list:
        if num2del in arr:
            arr.remove(num2del)
    return arr