# Task: Find the Missing Number
# Given an array of size n-1 with numbers from 1 to n, find the missing number

def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print("The missing number is:", find_missing([1, 2, 4, 5], 5))         # Output: 3
print("The missing number is:", find_missing([2, 3, 4, 7, 1, 6, 8, 9, 10], 10))  # Output: 5
