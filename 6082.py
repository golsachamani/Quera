n,m =[int(i) for i in input().split(' ')]
count = 0
for _ in range(n):
    setareh = input()
    count += setareh.count('*')
print(count)