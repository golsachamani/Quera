import math
n, k = list(map(int, input().split(' ')))
# list_jar = []
capasity = list(map(int,input().split(' ')))
# list_jar.append(capasity)
sum_capasity = sum(capasity)
requir_jars = int(math.ceil(sum_capasity/k))
max_jars = n - requir_jars
print(max_jars)
