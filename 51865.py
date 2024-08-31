def calculate(initial_score,travel_day):
    if travel_day==0:
        final_score = 20
    elif travel_day==7:
        final_score = initial_score
    else:
        final_score =max(initial_score- travel_day,0)
    return final_score
initial_score = int(input())
travel_day = int(input())
print(calculate(initial_score, travel_day))