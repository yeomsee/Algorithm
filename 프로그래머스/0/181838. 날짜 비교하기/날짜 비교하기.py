# My Code
def solution(date1, date2):
    for i in range(len(date1)):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
        else: # date1[i] == date2[i]
            if i == len(date1)-1:
                return 0