def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half, right_half = merge_sort(lst[:mid]), merge_sort(lst[mid:])
    merged, i, j = [], 0, 0
    while i < len(left_half) and j < len(right_half):
        merged.append(left_half[i]) if left_half[i] < right_half[j] else merged.append(right_half[j])
        i, j = i + 1 if left_half[i] < right_half[j] else i, j + 1
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [int(input("Enter an element: ")) for _ in range(5)]
print("\nUnsorted List:", my_list)

# Create a copy of the list for insertion sort
insertion_list = my_list.copy()

print("\nMerge Sorted List:", merge_sort(my_list))
insertion_sort(insertion_list)
print("\nInsertion Sorted List:", insertion_list)
