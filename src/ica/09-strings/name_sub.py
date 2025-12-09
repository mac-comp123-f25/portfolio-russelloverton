def count_words(word, text):
    num = 0
    ind_words = text.split()
    for i in ind_words:
        if i == word:
            num += 1
    return num

print(count_words("a", "a b c d a a a a"))