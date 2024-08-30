# My Code
def solution(num_list):
    def multiply(num_list):
        ret = 1
        for num in num_list:
            ret *= num
        return ret

    answer = sum(num_list) if len(num_list) >= 11 else multiply(num_list)
    return answer