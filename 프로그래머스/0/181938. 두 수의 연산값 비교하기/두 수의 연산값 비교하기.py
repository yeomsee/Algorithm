# My Code
def solution(a, b):
    return hap if (hap := int(str(a) + str(b))) > (gob := 2*a*b) else gob

# Simpler Code
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
