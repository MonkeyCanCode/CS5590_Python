#!/usr/bin/python3
# Lab assignment 2: part 4

import numpy as np

# Generate 15 random integers range from 0 to 20 inclusively into an array
data = np.random.randint(low=0, high=21, size=15)
# Get the unique number and count for each number
unique, counts = np.unique(data, return_counts=True)
# Find the highest occurrence
highest_occurrence = counts.max()
output = []
# Loop though unique and counts in a zip
for num, occurrence in zip(unique, counts):
    if occurrence == highest_occurrence:
        # Write num to the output if it has highest occurrence count
        output.append(num)
# Print the original data
print("Data: ", data)
print("Most frequent item(s) in the list is/are", output)