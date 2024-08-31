def multi_creation_table(n):
    for i in range(1, n+1):
        row =[]
        for j in range(1, n+1):
            row.append(i*j)
        print(' '.join(map(str,row)))
n = int(input())
multi_creation_table(n)