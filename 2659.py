n = int(input())
reference_string=input()
student_string = input()
mismatch_count = 0
for i in range(len(reference_string)):
    if reference_string[i] != student_string[i]:
        mismatch_count += 1
print(mismatch_count)



