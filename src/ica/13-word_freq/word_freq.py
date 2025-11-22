import string
full_words = []
dic = {}
def compute_frequencies(filename):
    file = open(filename, "r")
    lines = file.read()
    for line in lines.split("\n"):
        for word in line.split(" " or "--"):
            if word != "":
                word = word.strip(string.punctuation)
                full_words.append(word)
    for value in full_words:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    test_val = (list(tuple(dic.items())))
    test_val.sort()
    print(test_val)
    return dic


print(compute_frequencies("../TextFiles/alice.txt"))