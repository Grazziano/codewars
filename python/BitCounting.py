"""
Write a function that takes an integer as input, and returns the number of bits that are equal 
to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def count_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1  # Shift bits to the right by 1 to check the next bit
    return count

print(count_bits(1234))  # Output: 5
print(count_bits(7))     # Output: 3
print(count_bits(0))     # Output: 0
print(count_bits(1024))  # Output: 10
print(count_bits(2147483647))  # Output: 31
