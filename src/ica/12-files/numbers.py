def write_to_n(number, name):
    file = open(name, "w")
    for num in range(1, number):
        file.write(str(num) + "\n")

write_to_n(10, "../TextFiles/test.txt")