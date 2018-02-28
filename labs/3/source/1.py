#!/usr/bin/python3
# Lab assignment 3: part 1

"""
Data link: http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/
"""

import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Create empty variable to hold data for X and Y
x_data = []
y_data = []
# Populate data into x_data and y_data
with open("forestfires.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    # Skip header
    next(csv_reader)
    for line in csv_reader:
        temp = float(line[8])
        relative_humidity = float(line[9])
        wind = float(line[10])
        rain = float(line[11])
        area = 1 if float(line[12]) > 0 else 0
        x_data.append([temp, relative_humidity, wind, rain])
        y_data.append(area)
# Convert x_data and y_data into numpy array
np_x_data = np.array(x_data)
np_y_data = np.array(y_data)
# Create and build the model
model = LinearDiscriminantAnalysis()
model.fit(np_x_data, np_y_data)
# Perform prediction (may has a forest fire)
temp = 30
relative_humidity = 90
wind = 8
rain = 0.1
print("With temperature [%f] in Celcius, relative humidity [%f] of percent, wind speed [%f] in km/h, and rain [%f] in mm/m2" % (temp, relative_humidity, wind, rain))
if model.predict([[temp, relative_humidity, wind, rain]])[0]:
    print("It is likely to have a forest fire.")
else:
    print("It is not likely to have a forest fire.")
# Perform prediction (may not have a forest fire)
temp = 5
relative_humidity = 20
wind = 0.5
rain = 5.8
print("With temperature [%f] in Celcius, relative humidity [%f] of percent, wind speed [%f] in km/h, and rain [%f] in mm/m2" % (temp, relative_humidity, wind, rain))
if model.predict([[temp, relative_humidity, wind, rain]])[0]:
    print("It is likely to have a forest fire.")
else:
    print("It is not likely to have a forest fire.")
