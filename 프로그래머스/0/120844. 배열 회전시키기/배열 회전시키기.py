# My Code
def solution(numbers, direction):
    answer = []
    for i in range(len(numbers)):
        if direction == "left":
            answer.append(numbers[(i+1) % len(numbers)])
        else:
            answer.append(numbers[(i+len(numbers)-1) % len(numbers)])
            
    return answer

# Best Code
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
