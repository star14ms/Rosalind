from util import get_data

data = get_data(__file__)

words = data.split(' ')
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, count)