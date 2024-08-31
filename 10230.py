def check_triangle(a, b, c):

    if (a>0 and b>0 and c>0 and (a+b+c)==180):
        return "Yes"
    else:
        return "No"
a, b, c = [int(i) for i in input().split(' ')]
result = check_triangle(a, b, c)
print(result)