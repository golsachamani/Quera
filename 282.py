number=int(input())
result=0
for item in range(1,number):
    if number%item==0:
        result+=item
        
if result==number:
    print('Yes')
else:
    print('No')
# def is_perfect_number(number):

#     if number <= 0:

#         return False

#     divisors = []

#     for i in range(1, number):

#         if number % i == 0:

#             divisors.append(i)

#     sum_of_divisors = sum(divisors)

#     return sum_of_divisors == number

# # Input from the user

# num = int(float(input("Enter a positive integer: ")))

# if is_perfect_number(num):

#     print(f"{num} is a perfect number.")

# else:

#     print(f"{num} is not a perfect number.")