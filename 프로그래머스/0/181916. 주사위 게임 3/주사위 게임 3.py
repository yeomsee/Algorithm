# My Code
def solution(a, b, c, d):
    dice_list = [a, b, c, d]
    sorted_dice = sorted(dice_list, key=dice_list.count, reverse=True)
    new_dice_list = list(dict.fromkeys(sorted_dice))
    
    ''' dict.fromkeys(seq)를 사용하는 이유
        원래는 고유값을 가져오기 위해 set을 사용했으나
        set은 기존 list의 순서를 반영하지 못할 수 있기 때문!
        
        python 3.7부터 딕셔너리는 순서를 유지할 수 있다. 메모메모.
    '''
    
    if len(new_dice_list) == 1:
        p = new_dice_list[0]
        return 1111*p
    elif len(new_dice_list) == 2:
        p, q = new_dice_list[0], new_dice_list[1]
        if dice_list.count(p) != dice_list.count(q):
            return (10*p + q)**2
        return (p+q) * abs(p-q)
    elif len(new_dice_list) == 3:
        q, r = new_dice_list[1], new_dice_list[2]
        return q*r
    else: # len(new_dice_list) == 4
        return min(dice_list)

# Another Code
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)

'''
    사실 이게 조금 더 간단해 보이긴 한다 ㅎㅎ,,
'''
