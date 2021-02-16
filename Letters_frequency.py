str_of_words = [x.lower() for x in input().split()]
words_amount = {}

for word in str_of_words:
    if word not in words_amount:
        words_amount[word] = 1
    else:
        words_amount[word] += 1
        
for key, value in words_amount.items():
    print(key, value, end='')
    print()
