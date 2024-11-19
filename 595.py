def khp(n):
    if n == 1:
        return [[1]]
    else:
        result = khp(n - 1)
        prev_line = result[-1]
        last_line = [1]
        for i in range(len(prev_line) - 1):
            last_line.append(prev_line[i] + prev_line[i + 1])
        last_line.append(1)
        result.append(last_line)
        return result


n = int(input())
lines = khp(n)
for row in lines:
    print(" ".join(map(str, row)))
