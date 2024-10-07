# My Code
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        temp_list = []
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                if num//i == i:
                    temp_list.extend([i])
                else:
                    temp_list.extend([i, num//i])
                
        if len(temp_list)%2 == 0:
            answer += num
        else:
            answer -= num
    return answer