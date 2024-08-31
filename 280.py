def is_right_triangle(a, b, c):
    sides = sorted([a, b,c])
    return sides[2]**2 == sides[0]**2 + sides[1]**2
a = int(input())
b = int(input())
c = int(input())
if is_right_triangle(a, b,c):
    print('Yes') 
else:
    print('No') 