# Define the bubble_sort function which takes a list 'arr' as input
def bubble_sort(arr):
    n = len(arr)  # Get the length of the list

    # Outer loop to traverse the entire list
    for i in range(n):
        # Inner loop to compare adjacent elements
        # The range decreases with each pass since the largest elements "bubble" to the end
        for j in range(0, n - i - 1):
            # Compare current element with the next element
            if arr[j] > arr[j + 1]:
                # If they are in the wrong order, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Create a list of unsorted numbers
numbers = [64, 34, 25, 12, 22, 11, 90]

# Call the bubble_sort function to sort the list
bubble_sort(numbers)

# Print the sorted list
print("Sorted list in ascending order:", numbers)
