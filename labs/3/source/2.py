#!/usr/bin/python3
# Lab assignment 3: part 2

from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Load iris data
iris = datasets.load_wine()
# Load data and target into x and y
x = iris.data
y = iris.target
# Split the data with 20% of testing data and 80% of training data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print("SVM with linear kernel:")
# Create model for SVM with linear kernel
linear_kernel_model = svm.SVC(kernel="linear")
# Fit the data into the model
linear_kernel_model.fit(x_train, y_train)
# Generate y_predict from trained model with data from x_test
y_predict = linear_kernel_model.predict(x_test)
# Print data on both y_predicted and y_test
print("y_predicted:")
print(y_predict)
print("y_test:")
print(y_test)
# Check accuracy score by compare y_test and y_predicted
print("Accuracy score for SVM with linear kernel: %.3f" % metrics.accuracy_score(y_test, y_predict))

print("\nSVM with RBF kernel:")
# Create model for SVM with RBF kernel
rbf_model = svm.SVC(kernel="rbf")
# Fit the data into the model
rbf_model.fit(x_train, y_train)
# Generate y_predict from trained model with data from x_test
y_predict = rbf_model.predict(x_test)
# Print data on both y_predicted and y_test
print("y_predicted:")
print(y_predict)
print("y_test:")
print(y_test)
# Check accuracy score by compare y_test and y_predicted
print("Accuracy score for SVM with RBF kernel: %.3f" % metrics.accuracy_score(y_test, y_predict))