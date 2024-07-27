# My Code
def solution(before, after):
    before, after = list(before), list(after)
    before.sort()
    after.sort()
    
    if before == after:
        return 1
    return 0

# Simpler Code
'''
    굳이 list로 변환할 필요가 있었을까?
    sort() 함수는 리시트에서만 먹힌다고 생각했어서 그랬,,
'''

def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
