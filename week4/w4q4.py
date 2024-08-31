def iterate_lists(list1, list2):
    for i in range(len(list1)):
        print(f"List 1: {list1[i]}", f"List 2: {list2[-(i+1)]}")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_lists(list1, list2)
