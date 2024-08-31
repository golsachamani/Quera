substrings = ["MOLANA", "HAFEZ"]
n =5
lines = [input().strip() for _ in range(n)]

found_lines = []
for i in range(n):
    for substring in substrings:
        if substring in lines[i]:
            found_lines.append(i + 1)
            break

if found_lines:
    print(" ".join(map(str, found_lines)))
else:
    print("NOT FOUND!")
