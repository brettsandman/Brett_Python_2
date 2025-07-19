# Recursive function to compute the nth Fibonacci number
def fibonacci(n):
    # Step 1: Check if the input is 0
    # The 0th Fibonacci number is defined as 0
    if n == 0:
        return 0

    # Step 2: Check if the input is 1
    # The 1st Fibonacci number is defined as 1
    elif n == 1:
        return 1

    # Step 3: For n > 1, apply the recursive formula
    # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    # The function calls itself twice to calculate the two previous numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases to verify the function works correctly

# Step 4: Test the base case for n = 0
print("Fibonacci(0):", fibonacci(0))   # Expected output: 0

# Step 5: Test the base case for n = 1
print("Fibonacci(1):", fibonacci(1))   # Expected output: 1

# Step 6: Test for n = 2
# fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
print("Fibonacci(2):", fibonacci(2))   # Expected output: 1

# Step 7: Test for n = 3
# fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
print("Fibonacci(3):", fibonacci(3))   # Expected output: 2

# Step 8: Test for n = 5
# fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
print("Fibonacci(5):", fibonacci(5))   # Expected output: 5

# Step 9: Test for n = 10
# This will involve many recursive calls:
# fibonacci(10) = fibonacci(9) + fibonacci(8) = 34 + 21 = 55
print("Fibonacci(10):", fibonacci(10)) # Expected output: 55
