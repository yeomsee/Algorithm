# My Code
def solution(box, n):
    x, y, z = box[0], box[1], box[2]
    
    answer = (x//n) * (y//n) * (z//n)                
    return answer