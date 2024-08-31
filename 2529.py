# n = int(input())
# list = []
# for _ in range (n):
#     name =input()
#     list.append(name)
# charecter_list = [char for name in list for char in name]
# uniq_list = set(charecter_list)
# print(len(uniq_list))

list = []
n= int(input())
for _ in range(n):
    word = input()
    list.append(word)
list2 =[]    
for i in list:
    list2.append(len(set(i)))
print(max(list2))

