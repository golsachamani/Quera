a, b = [int(i) for i in input().split(' ')]
real_min = 0 if b == 0 else 60-b
real_hour = 0 if a==0 else(12-a)


print(f'{real_hour:02}:{real_min:02}')
