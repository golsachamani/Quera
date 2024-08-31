number = []
while True:
    n= int(input())
    if n==0:
        break
    number.append(n)

for num in reversed(number):
    print(num)