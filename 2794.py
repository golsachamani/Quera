x1,y1 = [int(i) for i in  input().split(' ')]
x2,y2 = [int(i) for i in input().split(' ')]
x3,y3 = [int(i) for i in input().split(' ')]


if x1 ==x2:
    x4 =x3
elif x1==x3:
     x4=x2
else:
     x4=x1 


if y1 ==y2:
    y4=y3
elif y1==y3:
    y4=y2
else:
    y4=y1

print(x4,y4)
    