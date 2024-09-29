# BUBBLE SORT

def bubble_sort(values):
    for i in range(0, len(values) - 1):
        for j in range(len(values) - 1):
            if (values[j] > values[j+1]):
                values[j], values[j+1] = values[j+1], values[j]

values = [5,2,9,4,6]
print(f"Unsorted numbers: {values}")
bubble_sort(values)
print(f"Sorted numbers using Bubble Sort: {values}")