def factorial(n):
    """
    Recursive function to compute the factorial of a non-negative integer n.
    """
    # Step 1: Check for invalid input (negative number)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Step 2: Base case – factorial of 0 is 1
    elif n == 0:
        return 1

    # Step 3: Recursive case – multiply n by factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Test cases to verify the function
def test_factorial():
    print("Testing factorial function...")

    # Step 4: Test base case
    assert factorial(0) == 1, "Test case 0! failed"

    # Step 5: Test small values
    assert factorial(1) == 1, "Test case 1! failed"
    assert factorial(2) == 2, "Test case 2! failed"
    assert factorial(3) == 6, "Test case 3! failed"
    assert factorial(4) == 24, "Test case 4! failed"
    assert factorial(5) == 120, "Test case 5! failed"

    # Step 6: Test a larger value
    assert factorial(10) == 3628800, "Test case 10! failed"

    # Step 7: If all assertions pass, print success message
    print("All test cases passed.")

# Step 8: Run the test function
test_factorial()
