r, c = [int(i)for i in input().split(' ')]
r_move = 11-r
if 1<=c<=10:
    direction = 'right'
    c_move = c
else:
    direction= 'left'
    c_move = 21-c
print(direction,r_move,c_move)
    