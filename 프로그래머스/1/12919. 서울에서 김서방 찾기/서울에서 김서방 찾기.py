# My Code
def solution(seoul):
    for i, p in enumerate(seoul):
        if p == "Kim":
            return f"김서방은 {i}에 있다"

# Best Code
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
