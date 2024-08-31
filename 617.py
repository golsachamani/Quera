number = int(input())
list = [int(i) for i in str(number)]
reversed_list = list[::-1]
# print(reversed_list)
if reversed_list==list:
    print('YES')
else:
    print('NO')