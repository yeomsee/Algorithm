# My Code
def solution(spell, dic):
    for word in dic:
        if all(string in word for string in spell):
            return 1
    return 2