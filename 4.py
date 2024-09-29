# MERGE SORT

def merge_sort(values):
    if len(values) > 1:
        left_value = values[:len(values)//2]
        right_value = values[len(values)//2:]

        merge_sort(left_value)
        merge_sort(right_value)

        i = 0
        j = 0
        k = 0

        while i < len(left_value) and j < len(right_value):
            if left_value[i] < right_value[j]:
                values[k] = left_value[i]
                i += 1
            else:
                values[k] = right_value[j]
                j += 1
            k += 1

        while i < len(left_value):
            values[k] = left_value[i]
            i += 1
            k += 1

        while j < len(right_value):
            values[k] = right_value[j]
            j += 1
            k += 1

values = [5,2,9,4,6]
print(f"Unsorted numbers: {values}")
merge_sort(values)
print(f"Sorted numbers using Merge Sort: {values}")