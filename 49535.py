n,k = [int(i) for i in input().split(' ')]
capacities = []
for _ in range(n):
    capacities.append(int(input()))
    total_capacity = sum(capacities)

if total_capacity >= k:
    print("YES")
else:
    print("NO")