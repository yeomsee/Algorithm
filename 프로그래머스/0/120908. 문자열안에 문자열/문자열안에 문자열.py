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