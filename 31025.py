import math
n,k = [int(i) for i in input().split(' ')]
for _ in range(k):
    n/=2
result = math.floor(n)
print(result)