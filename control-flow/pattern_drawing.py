#!/usr/bin/py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print each asterisk in the current row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
