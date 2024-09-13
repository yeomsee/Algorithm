# My Code
def solution(strArr):
    len2freq = {}
    for string in strArr:
        if len(string) not in len2freq.keys():
            len2freq[len(string)] = 1
        else:
            len2freq[len(string)] += 1
            
    for k, v in len2freq.items():
        if v == max(len2freq.values()):
            return v