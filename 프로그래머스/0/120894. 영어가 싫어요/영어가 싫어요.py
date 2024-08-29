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