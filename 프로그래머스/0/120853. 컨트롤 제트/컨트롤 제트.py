# My Code
def solution(s):
    s = s.split()
    for i in range(len(s)):
        if s[i] == "Z":
            s[i] = -int(s[i-1])
    
    answer = sum([int(num) for num in s])
    return answer

# Another Code .. 스택 이용
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
