# My Code
def solution(my_string):
    answer = [0]*52
    for string in my_string:
        if "A" <= string and string <= "Z":
            answer[int(ord(string)%ord("A"))] += 1
        elif "a" <= string and string <= "z":
            answer[int(ord(string)%ord("a")) + 26] += 1
            
    return answer