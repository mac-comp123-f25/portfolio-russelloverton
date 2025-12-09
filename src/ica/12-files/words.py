def i_words(name):
    file = open(name, "r")
    file_contents = file.read()
    i_words = []
    for word in file_contents.split(" " or "\n"):
        for char in word:
            if char == "i":
                i_words.append(word)
    return i_words



print(i_words("../TextFiles/alice.txt"))