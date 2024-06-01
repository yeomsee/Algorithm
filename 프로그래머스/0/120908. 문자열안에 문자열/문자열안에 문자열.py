# My Code
def solution(str1, str2):
    # i는 str1의 위치를 움직이는 index
    for i in range(len(str1)):
        # j는 str2의 위치를 움직이는 index
        for j in range(len(str2)):
            # prevent 'index out of range'
            if i+j < len(str1):
                if str1[i+j] != str2[j]:
                    break
                if j == (len(str2) - 1):
                    return 1
    return 2

'''
    자료구조 때 배웠던 String Matching의 Naive Version을 생각하면서 구현해봤다.
    파이썬 스타일이라기보다는 오히려 C, C++ 느낌이 나는 거 같다.
'''

# Best Code
def solution(str1, str2):
    return 1 if str2 in str1 else 2

'''
    사실 처음에는 이걸로 했는데 Error가 떠서 포기했었는데 후,, 오타가 있었나보다
'''
