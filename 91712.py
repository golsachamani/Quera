x1,x2= [int(i) for i in input().split(' ')]
if x1 == x2:
    print("Saal Noo Mobarak!")
elif x1 < x2:
    print('R' * (x2 - x1))
else:
    print('L' * (x1 - x2))