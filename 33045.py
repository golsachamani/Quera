def divisor(a):
    result = []
    for i in range(1, a+1):
        if a % i == 0:
            result.append(i)
    return result
n= int(input())
all_divisors = []
for i in range(1, n+1):
    i_divisors = divisor(i)
    all_divisors.extend(i_divisors)
count = len(all_divisors)
all_sum = sum(all_divisors)
print(count,all_sum)


