n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = sum(a[i] * b[i] for i in range(n))


print(total)