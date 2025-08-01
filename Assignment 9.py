# Define merge_sort function to sort a list of strings alphabetically
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # A list of 0 or 1 element is already sorted

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half

    # Merge the two sorted halves
    return merge(left_half, right_half)

# Define merge function to combine two sorted lists
def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge elements in alphabetical order
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
words = ["Banana", "apple", "Cherry", "date", "Elderberry", "fig", "grape"]
sorted_words = merge_sort(words)
print("Sorted list in alphabetical order:", sorted_words)
