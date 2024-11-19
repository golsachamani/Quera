def is_any_zero(ch):
    for a in ch:
        if a==0:
            return True
    return False
chaclote_dish = list(map(int, input().split(' ')))
chaclate_eaten = [0,0,0,0]
i = 0
while not is_any_zero(chaclote_dish):
    chaclote_dish[i] -= 1
    chaclate_eaten[i] +=1
    chaclote_dish.append(chaclote_dish.pop(0))
    i +=1
    i %=4
print(' '.join(map(str,chaclate_eaten)))

