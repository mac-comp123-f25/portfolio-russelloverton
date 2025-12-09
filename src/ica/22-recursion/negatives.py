def count_negatives(lst):
    if lst == []:
        return 0
    elif(lst[0] < 0):
        return 1 + count_negatives(lst[1:])
    else:
        return count_negatives(lst[1:])

print(count_negatives([-1, -2, -3, -4, -5, 5, 2, 2, 2]))
