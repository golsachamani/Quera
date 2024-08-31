a,b,l = [int(i) for i in input().split(' ')]

if l%2==0:
    print((l//2)*(a+b))
else:
    print(((l-1)//2)*(a+b)+a)