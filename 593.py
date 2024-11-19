def sum_digit(num):
    return sum(int(digit) for digit in str(num))

def is_prime(n):
    if n==2:
        return True
    for i in range(2,int(n**0.5) +1):
        if n%i ==0:
            return False
    return True

def find_prime_number(num,b):
    count = 0
    for i in range(num+1,10**7):
        if is_prime(i):
            count+=1
            if count==b:
                return i


num = int(input())
b = sum_digit(num)
result=find_prime_number(num,b)
print(result)


