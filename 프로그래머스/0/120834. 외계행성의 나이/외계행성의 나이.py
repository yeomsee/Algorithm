# My Code
def solution(age):
    age = str(age)
    answer = ''.join([chr(ord('a') + int(num)) for num in age])
    return answer

# Another Code : 원래 하려고 했던 것 .. 사실 이게 좀 더 직관적인 거 같다.
def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))

# Another Code2
def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

'''
    단순하지만 이것도 꽤나 직관적인 거 같다.
'''
