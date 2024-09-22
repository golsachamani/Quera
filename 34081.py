n ,k =[ int(i) for i  in input().split(' ')]
current_position = 0
step =0
while True:
    current_position = (current_position+k)%n
    step+=1
    
    if current_position ==0:
        break
print(step)