def print_abbrev(name):
    file = open(name, "r")
    for line in file:
        text_line = line.strip()
        sliced = slice(text_line [0:20])
        print(sliced)
    file.close()

print_abbrev("../TextFiles/alice.txt")