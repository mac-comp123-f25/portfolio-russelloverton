bed_len = 30
bed_width = 3.5


flower_rows = bed_width * 2
flower_cols = bed_len * 2
flower_count = flower_rows * flower_cols


print("Your garden has a length of", bed_len, "and a width of", bed_width)
print("This allows us to have", int(flower_rows), "rows and", int(flower_cols), "columns.")
print("This means that we can fit", int(flower_count), "flowers in the garden.")