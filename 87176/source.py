def game(number):
    list =[int(digit) for digit in str(number)]
    return max(list) - min(list)

