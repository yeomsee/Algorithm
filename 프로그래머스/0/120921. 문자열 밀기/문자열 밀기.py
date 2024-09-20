# My Code
def solution(A, B):
    count = 0
    org_A = A
    while True:
        if A == B:
            return count
        
        # PUSH
        A = A[-1] + A[:-1]
        count += 1
        
        # COMPARE
        if org_A == A:
            return -1