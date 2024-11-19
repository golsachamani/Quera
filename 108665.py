n = input()
list_word = list(n)
list_vom = [char for char in list_word if char in 'aeiou']
print(len(list_vom)*2)