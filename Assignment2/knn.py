# -------------------------------------------------------------------------
# AUTHOR: Zhong Ooi
# FILENAME: knn.py
# SPECIFICATION: using data to do knn calculation and finding if the accuracy of 1NN
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
# loop your data to allow each instance to be your test set

#integer to store the correct predictions
correct_prediction = 0
for i, instance in enumerate(db):
    # print(i,instance)
    X = []
    Y = []
    # add the training features to the 2D array X and remove the instance that will
    # be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid
    # warning messages
    # transform the original training classes to numbers and add them to the vector
    # Y. Do not forget to remove the instance that will be used for testing in this iteration.
    # For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages
    # --> add your Python code here

    # turn the csv data into usable float data
    for data in db:
        temp = []
        for num in data[:2]:
            temp.append(float(num))
        X.append(temp)
        if data[2] == "+":
            Y.append(2.0)
        else:
            Y.append(1.0)
    # remove the data sample for testing
    test_Sample = [X.pop(i), Y.pop(i)]


    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)
    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([test_Sample[0]])[0]

    # compare the prediction with the true label of the test instance to start
    # calculating the error rate.
    # --> add your Python code here
    if class_predicted == test_Sample[1]:
        correct_prediction += 1
# print the error rate
print("error rate:", (len(db) - correct_prediction) / len(db))
