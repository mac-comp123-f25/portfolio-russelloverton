def remove_all(value, set):
    while set.count(value) > 0:
        set.remove(value)

thing = ["lists", "are", "dumb"]
remove_all("are", thing)
print(thing)