def count_occurrences(tup, item):
    count = 0
    for elem in tup:
        if elem == item:
            count += 1
    return count


tp1 = (50, 10, 60, 70, 50, 32, 50)
item_to_count = 50

occurrences = count_occurrences(tp1, item_to_count)
print(f"The number of occurrences of {item_to_count} is: {occurrences}")
