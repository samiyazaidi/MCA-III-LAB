import numpy as np

array = np.array([[5, 2, 9, 1],
                  [7, 6, 4, 3],
                  [8, 1, 2, 9],
                  [4, 3, 5, 6]])

print("Original Array:")
print(array)

sorted_indices_row = np.argsort(array[1, :])
sorted_by_row = array[:, sorted_indices_row]

print("\nSorted by Second Row:")
print(sorted_by_row)

sorted_indices_column = np.argsort(array[:, 1])
sorted_by_column = array[sorted_indices_column, :]

print("\nSorted by Second Column:")
print(sorted_by_column)
