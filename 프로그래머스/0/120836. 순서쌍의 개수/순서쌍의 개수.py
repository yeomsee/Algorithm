# My code
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append((i, n*i))
            
    return len(answer)

# Another Code (Simpler Ver.)
def solution(n):
    return len([number for number in range(1, n+1) if n%number == 0])

'''
    어차피 갯수만 세면 되는 거니까 굳이 append까지 할 필요는 없었을 듯
'''
