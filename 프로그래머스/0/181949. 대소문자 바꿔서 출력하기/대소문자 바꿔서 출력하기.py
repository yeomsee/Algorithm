# My Code
strings = input()
print(''.join([string.upper() if string == string.lower() else string.lower() for string in strings]))

# Best Code
print(input().swapcase())
