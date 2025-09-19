def string_of_nums(num):
    result = ""
    for i in range(num):
        result += " " + str(i)
    return result

print(string_of_nums(100))