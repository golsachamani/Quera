n = input()
for i in range (len(n)):
    word = n[i]*(i+1)+n[i+1:]
    print(word)