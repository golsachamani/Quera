T= int(input()) 
if T>-273 and T<= 6000:
   
    if T>100:
        print('Steam')
    elif T <0:
        print('Ice')
    else:
        print('Water')