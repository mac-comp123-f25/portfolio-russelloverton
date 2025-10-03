def smallest_diff(x, y, z):
    print('smallest_diff inputs:', x, y, z)
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff

#Local environment
#   x    3
#   y    9
#   z    5
#   diff1  6
#   diff2  4
#   diff3  2
#   min_diff 2

print(smallest_diff(3, 9, 5))