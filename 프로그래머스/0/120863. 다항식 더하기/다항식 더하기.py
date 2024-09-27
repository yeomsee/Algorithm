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