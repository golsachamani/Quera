
n = int(input())
print("*"*n)
space = ' '*(n-2)
line_with_space = '*' + space + '*'
for i in range(n-2):
    print(line_with_space)
print("*"*n)
