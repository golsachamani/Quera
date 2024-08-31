def is_prime(n):
    if n <= 1:
        return False
    if n == 2 :
        return True 
    if n % 2 == 0:
        return False 
    # for i in range(3, int(n**0.5) + 1, 2):
    for i in range(3, int(math.ceil(n**0.5)), 2):
        if n % i == 0:
            return False
    return True

def find_primes_between(start, end):
    primes = []
    for num in range(start+1, end):
        if is_prime(num):
            primes.append(num)
    return primes
            
    
    
start = int(input())
end = int(input())
result =find_primes_between(start, end)

print(','.join(map(str,result)))  

