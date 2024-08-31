# def fib(a):
#     if a == 0 or a==1:
#         return 1
#     elif a==2:
#         return 2
#     else:
#         return fib(a-1)+fib(a-2)

# def fib_sequence(mx):
#     list =[]
#     i=1
#     while True:
#         list.append(fib(i))
#         if list[-1]>=mx:
#             break
#         i+=1
#         return list
# n = int(input())
# seq = fib_sequence(n)
# result = ''
# print(result)

def is_fibonacci(num):
    fibs = [1, 2]
    while fibs[-1] < num:
        fibs.append(fibs[-1] + fibs[-2])
    return num in fibs

def generate_signs(n):
    signs = []
    for i in range(1, n + 1):
        if is_fibonacci(i):
            signs.append('+')
        else:
            signs.append('-')
    return ''.join(signs)


n = int(input())
result = generate_signs(n)
print(result)