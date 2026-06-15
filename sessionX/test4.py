text = int(input())
for _ in range(text):
    str = input().split()
    result =[]

    for word in str:
        new_word =""
        for i in range(len(word)):
            if i%2==0:
                new_word+=word[i].upper()
            else:
                new_word+=word[i].lower()
        result.append(new_word)
    print(" ".join(result))


