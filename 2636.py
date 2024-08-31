base =[1,1,2,2,2,8]
current = [int(i) for i in input().split(' ')]
result =[base[i] -current[i] for i in range(6)]
print(' '.join(map(str,result)))