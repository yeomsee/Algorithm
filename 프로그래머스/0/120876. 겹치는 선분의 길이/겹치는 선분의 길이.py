# My Code
def solution(lines):
    inter_set = [set(range(p1, p2)) for p1, p2 in lines]
    
    inter1 = inter_set[0]&inter_set[1]
    inter2 = inter_set[0]&inter_set[2]
    inter3 = inter_set[1]&inter_set[2]

    total_inter = inter1 | inter2 | inter3
    return len(total_inter)