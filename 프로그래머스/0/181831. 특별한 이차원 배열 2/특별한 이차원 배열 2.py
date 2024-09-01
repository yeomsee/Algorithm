# My Code
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# Best Code
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))

'''
    * zip 기본 문법
    >>> numbers = [1, 2, 3]
    >>> letters = ["A", "B", "C"]
    >>> for pair in zip(numbers, letters):
    ...     print(pair)
    ...
    (1, 'A')
    (2, 'B')
    (3, 'C')

    * zip 병렬 처리
    >>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
        ...     print(number, upper, lower)
        ...
        1 A a
        2 B b
        3 C c
        4 D d
        5 E e

    => 전치행렬을 이용한 아주 기똥찬 풀이다,, 진짜 지렸다
'''
