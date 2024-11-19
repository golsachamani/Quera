num1 = int(input())
operator = input()
num2 = int(input())
if operator=="+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1*num2
elif operator == '/':
    if num2!= 0:
        result = num1/num2
print(result)