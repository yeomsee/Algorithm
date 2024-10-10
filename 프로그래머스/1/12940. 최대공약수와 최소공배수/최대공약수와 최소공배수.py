# My Code
def solution(n, m):
    m, M = min(n, m), max(n, m)
    
    temp_list = []
    for i in range(1, int(m**0.5) + 1):
         if m%i == 0:
            temp_list.extend([i, m//i])
    
    for x in sorted(temp_list, reverse=True):
        if M%x == 0:
            gcd = x
            lcm = gcd * (M//x) * (m//x)
            return [gcd, lcm]
        