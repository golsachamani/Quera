shirt_size = list(map(int, input().split()))  
person_size = list(map(int, input().split())) 


if shirt_size[0] >= person_size[0] and shirt_size[1] >= person_size[1]:
    print("yes")
else:
    print("no")