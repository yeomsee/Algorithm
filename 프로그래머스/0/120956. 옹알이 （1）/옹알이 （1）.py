# My Code
def check_string(string):
    patterns = ["aya", "ye", "woo", "ma"]
    
    while len(string) > 0:
        matched = False
        for pattern in patterns:
            
            if string.startswith(pattern):
                string = string[len(pattern):]
                matched = True
                break
        
        if not matched:
            return False
    
    return True

def solution(babbling):
    count = 0
    for b in babbling:
        if check_string(b):
            count += 1
            
    return count