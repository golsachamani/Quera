n = int(input())
sentence = input().split(' ')
reverse_sentence = sentence[::-1]

print(' ' .join(map(str,reverse_sentence)))