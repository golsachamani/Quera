n = int(input())
for i in range(0,n):
    if 2**i <=n and 2**(i+1) > n:
        print(2**(i+1))
        break
    