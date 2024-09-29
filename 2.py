# SELECTION SORT

def selection_sort(values):
    for i in range(0, len(values) - 1):
        current_minimum_value = i
        for j in range(i + 1, len(values)):
            if values[j] < values[current_minimum_value]:
                current_minimum_value = j

        values[i], values[current_minimum_value] = values[current_minimum_value], values[i]

values = [5,2,9,4,6]
print(f"Unsorted numbers: {values}")
selection_sort(values)
print(f"Sorted numbers using Selection Sort: {values}")