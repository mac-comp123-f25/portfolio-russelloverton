def every_other(thing):
    length = len(thing)
    return thing[::2]

def sum_positive(litht):
    total = 0
    for i in litht:
        if i > 0:
            total += i
    return total

thingy = ("lists", "are", "dumb")
print(every_other(thingy))
print(sum_positive((-10,0,1,2,3,4,5,6)))
