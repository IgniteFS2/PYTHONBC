sentence = input("Please input a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Output:", word_count)
