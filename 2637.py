def max_parts(n):
    h = n // 2
    v = n - h
    return (h + 1) * (v + 1)


n = int(input())
print(max_parts(n))