# My Code
def solution(polynomial):
    poly_list = polynomial.replace(" ", "").split("+")
    
    x_count, c_count = 0, 0
    for poly in poly_list:
        if "x" in poly:
            if poly == "x":
                x_count += 1
            else:
                x_count += int(poly[:-1])
        else: # constant
            c_count += int(poly)
    
    if x_count == 0:
        return f"{c_count}"
    else:
        if c_count == 0:    
            return f"{x_count}x" if x_count != 1 else "x"
        return f"{x_count}x + {c_count}" if x_count != 1 else f"x + {c_count}"

''' 깨달은 점
    1. strip()의 경우 그냥 공백제거가 아님
    → 정확히 말해서는 '양 옆' 공백 제거임
    2. 반례를 잘 생각하자
    → 이 문제 많이 헷갈렸던 이유
    : 처음에는 x의 계수가 1인 경우를 고려하지 못 했다.
    : 그 다음에는 x의 계수가 한 자리수인 것만 생각해서 11번째 줄 코딩을 x_count += int(poly[0])과 같이 구현한 것,,!
'''
