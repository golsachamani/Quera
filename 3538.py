
days = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']
user_data = {}

for i in range(3):
    n = input()
    user_input = input().split(' ')
    
    for day in days:
        if day in user_input:
           
            user_data[day] = user_input

missing_days = len(days) - len(user_data)

# print( user_data)
print( missing_days)
