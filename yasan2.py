number_students = int(input(" "))

entry_fee_per_student = 20
snack_fee_per_student = 5
van_capacity = 10
van_rent_per_van = 150

total_entry_fee = number_students * entry_fee_per_student
total_snack_fee = number_students * snack_fee_per_student

num_vans = (number_students + van_capacity - 1) // van_capacity
total_van_rent = num_vans * van_rent_per_van

total_cost = total_entry_fee + total_snack_fee + total_van_rent

print(f" {total_entry_fee} ")
print(f" {total_snack_fee} ")
print(f" {num_vans}")
print(f"{total_van_rent} ")
print(f"{total_cost} ")
