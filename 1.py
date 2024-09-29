# INSERTION SORT

def insertion_sort(values):
    for i in range(1, len(values)):
        j = i
        while values[j - 1] > values[j] and j > 0:
            values[j - 1], values[j] = values[j], values[j - 1]
            j -= i

values = [5,2,9,4,6]
print(f"Unsorted numbers: {values}")
insertion_sort(values)
print(f"Sorted numbers using Insertion Sort: {values}")