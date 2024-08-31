
def reverse_number(n):
   return int(str(n)[::-1])


num1 = int(input(""))
num2 = int(input(""))

reversed_num1 = reverse_number(num1)
reversed_num2 = reverse_number(num2)

if reversed_num1 < reversed_num2:
    print(f"{num1} < {num2}")
elif reversed_num1 > reversed_num2:
    print(f"{num2} < {num1}")
else:
    print(f"{num1} = {num2}")
