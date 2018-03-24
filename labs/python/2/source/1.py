#!/usr/bin/python3
# Lab assignment 2: part 1

# User data from the lab
data = {"python": 50, "web": 30, "c": 20, "java": 40}
begin_value = 30
end_value = 40
print("For range", begin_value, "to", end_value)

# Create an empty list to hold the data
output = []
for key, value in data.items():
    # Check if value is within the range inclusively
    if begin_value <= value <= end_value:
        output.append(key)

print("You can purchase books", output)
