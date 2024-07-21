# My Code
def solution(emergency):
    answer_list = []
    sorted_emergency = list(reversed(sorted(emergency)))
    for num in emergency: # 정렬되지 않은 리스트에서
        index = sorted_emergency.index(num) # 각 value가 정렬된 리스트에서 몇 번째인지?
        answer_list.append(index+1)
    return answer_list