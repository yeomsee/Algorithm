# My Code
def solution(numbers):
    eng2num_dict = {"zero" : '0',
                    "one" : '1',
                    "two" : '2',
                    "three" : '3',
                    "four" : '4',
                    "five" : '5',
                    "six" : '6',
                    "seven" : '7',
                    "eight" : '8',
                    "nine" : '9'}
    
    answer = ''
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            temp = numbers[i:j+1]
            if temp in eng2num_dict.keys():
                answer += eng2num_dict[temp]
                i = j+1
                break
    answer = int(answer)
    return answer

# Best Code
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

'''
    enumerate와 replace를 이용해서 완전 편하게 풀 수도 있음..!
'''
