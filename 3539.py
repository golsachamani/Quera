def splite_num(number):
    
    if number<0:
        raise ValueError
    while number>=10:
        
        number= sum(int(i) for i in str(number))
    return number
   
   
number = int(input())
result=splite_num(number)
print(result)


