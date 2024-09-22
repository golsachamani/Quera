list =[]
n = int(input())
for _ in range(n):
    list.append( int(input()))
    
change_count = 0
for i in range(1, n):
    if list[i] != list[i - 1]:
        change_count += 1
print(change_count)