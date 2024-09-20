# My Code
def solution(a, b):
    def get_gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a%i == 0 and b%i == 0:
                return i
            
    gcd = get_gcd(a, b)
    b = int(b/gcd)
    
    for x in range(2, b+1):
        if (b%x == 0) and (x%2 != 0 and x%5 != 0):
            return 2
    return 1