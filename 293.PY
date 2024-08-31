def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    for num in primes:
        print(num)           
    
    
start = int(input())
end = int(input())

find_primes_between(start, end)

