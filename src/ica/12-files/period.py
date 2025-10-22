def up_to_period(name):
    file = open(name, 'r')
    text = file.read()
    full_string = ""
    for char in text:
        full_string += char
        if char == ".":
            return full_string


print(up_to_period("../TextFiles/emma.txt"))