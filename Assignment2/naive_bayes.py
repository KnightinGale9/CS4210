# -------------------------------------------------------------------------
# AUTHOR: Zhong Ooi
# FILENAME: naive_bayes.py
# SPECIFICATION: calculating naive_bayes using testing data
#                to create a model and testing data to test the model
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv


# reading the training data in a csv file
# --> add your Python code here
dbTraining = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)
# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
#feature values for each attribute including classes
feature_values = {1: {'Sunny': 1, 'Overcast': 2, 'Rain': 3}, 2: {'Cool': 1, 'Mild': 2, 'Hot': 3},
                  3: {'Normal': 1, 'High': 2}, 4: {'Weak': 1, 'Strong': 2}, 5: {'Yes': 1, 'No': 2}}
temp = []
X = []
Y = []
for instance in dbTraining:
    for i, value in enumerate(instance):  # retriving the feature values
        # using feature_values to get the number values and adding to a list
        if i == 0:
            continue
        temp.append(feature_values[i][value])
    # adding to vector X
    X.append(temp[:len(instance) - 2].copy())
    # adding to Vector Y
    Y.append(temp[len(instance) - 2])
    # clear temp to be used again
    temp.clear()

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)
# reading the test data in a csv file
# --> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)
# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) +
      "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) +
      "Confidence".ljust(15))
# use your test samples to make probabilistic predictions. For instance:
# clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here
XTest = []
for instance in dbTest:
    for i, value in enumerate(instance):  # retriving the feature values
        # using conversion to get the number values and adding to a list
        if i == 0:
            continue
        if i == len(instance) - 1:
            continue
        temp.append(feature_values[i][value])
    # adding to vector X
    XTest.append(temp[:len(instance) - 2].copy())
    # clear temp to be used again
    temp.clear()
# print(len(XTest),XTest)
result = []
for data in XTest:
    result.append(clf.predict_proba([data])[0])

#printing the instance data
for i, classResult in enumerate(result):
    # print(classResult)
    if classResult[0] >= classResult[1]:
        if classResult[0] > 0.75:
            print(dbTest[i][0].ljust(14), dbTest[i][1].ljust(14), dbTest[i][2].ljust(14),
                  dbTest[i][3].ljust(14), dbTest[i][4].ljust(14), "Yes".ljust(14), round(classResult[0], 2))
    else:
        if classResult[1] >= 0.75:
            print(dbTest[i][0].ljust(14), dbTest[i][1].ljust(14), dbTest[i][2].ljust(14),
                  dbTest[i][3].ljust(14), dbTest[i][4].ljust(14), "No".ljust(14), round(classResult[1], 2))


