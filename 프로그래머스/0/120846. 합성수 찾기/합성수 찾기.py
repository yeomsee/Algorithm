# My Code
def solution(n):
    answer_list = []
    for i in range(1, n+1):
        count = 0
        for x in range(1, i+1):
            if i%x == 0:
                count += 1
        if count >= 3:
            answer_list.append(x)
            
    return len(answer_list)

# Best Code
def solution(n):
    output = 0
    for i in range(4, n + 1): # 4부터 모든 수에 대해서 반복
        for j in range(2, int(i ** 0.5) + 1): # 2부터 i의 제곱근까지의 수에 대해서만 반복
            if i % j == 0: # i가 합성수라면
                output += 1
                break # 더 이상 수행할 필요가 없음
    return output


'''
    사실 'NOT 소수 = 합성수'이므로
    내 풀이처럼 count를 굳이 안 써도 됐을 거 같긴 하다,,,
'''
