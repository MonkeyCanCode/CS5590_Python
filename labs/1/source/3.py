#!/usr/bin/python3
# Lab assignment 1: part 3


def find_triplets(numbers):
    """
    Print triplets in the list which gives the sum of zero.
    """
    numbers_length = len(numbers)
    for i in range(numbers_length - 2):
        for j in range(i + 1, numbers_length - 1):
            for k in range(j + 1, numbers_length):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    print(numbers[i], numbers[j], numbers[k])


# Sample inputs from lab 1
user_numbers = [1, -7, 6, 2, -1, 2, 0, -2, 0]
print("Here are the triplets found the input provided above:")
# This will print out all possible combinations (with duplicates due to duplicate inputs)
find_triplets(user_numbers)
