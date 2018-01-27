#!/usr/bin/python3
# Lab assignment 1: part 4

# Generate the data for students and classes
student_classes = [
    ("Student 0", "Python"),
    ("Student 0", "Web Application"),
    ("Student 1", "Python"),
    ("Student 2", "Web Application"),
    ("Student 3", "Python"),
    ("Student 3", "Web Application"),
    ("Student 4", "Python"),
    ("Student 5", "Web Application")
]

# Create an empty dictionary
student_class_dict = {}

# Add data into dictionary: student's name is key and student's classes are values
for student_class in student_classes:
    if student_class[0] in student_class_dict:
        student_class_dict[student_class[0]].append(student_class[1])
    else:
        student_class_dict[student_class[0]] = [student_class[1]]

# Create list for holding students who are taking both classes
both = []
# Create list for holding students who are only taking one class
single = []

# Push data into 'both' and 'single' lists based on the number of values for each key
for k, v in student_class_dict.items():
    if len(v) != 2:
        single.append(k)
    else:
        both.append(k)

print("Both classes: {", both, "}")
print("Single class: {", single, "}")
