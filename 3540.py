# n,x,y = [int(i) for i in input().split(' ')]
# for a in range(n//x+1):
#     if (n-a*x)%y==0:
#         b = (n-a*x)//y
#         print(a,b)
#     else:
#         print(-1)

def find_solution(n, x, y):
    # Check if it's possible to reach exactly n using combinations of x and y
    for a in range(n // x + 1):  # a ranges from 0 to n//x
        if (n - a * x) % y == 0:
            b = (n - a * x) // y
            return a, b
    return -1

# Input reading
n, x, y = map(int, input().split())

# Find the solution
result = find_solution(n, x, y)

# Output the result
if result == -1:
    print(result)
else:
    print(result[0], result[1])