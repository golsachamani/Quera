def check_health_label(label):
    red_count = label.count('R')
    yellow_count = label.count('Y')
    green_count = label.count('G')
    
    if red_count >= 3:
        print("nakhor lite")
    elif red_count >= 2 and yellow_count >= 2:
        print("nakhor lite")
    elif green_count == 0:  
        print("nakhor lite")
    else:
        print("rahat baash")

label = input()
    
check_health_label(label)