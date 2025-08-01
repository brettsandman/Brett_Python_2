# Define the quick_sort function
def quick_sort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here we use the last element)
    pivot = arr[-1]

    # Create sub-arrays for elements less than and greater than the pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively sort the left and right sub-arrays, and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
numbers = [33, 10, 55, 71, 29, 3, 94, 21]
sorted_numbers = quick_sort(numbers)
print("Sorted list in ascending order:", sorted_numbers)
