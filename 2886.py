a,b = [int(i) for i in input().split(' ')]
real_min = (60-b)%60
real_hour = (12-a)%12
# if real_min!= 0:
#     real_hour = (real_hour-1)%12

real_hour = f'{real_hour:02}'
real_min = f'{real_min:02}'
print(real_hour,real_min)