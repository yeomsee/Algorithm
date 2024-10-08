# My Code
def solution(price, money, count):
    total_price = sum([(i+1)*price for i in range(count)])
    if total_price <= money:
        return 0
    return (total_price)-money