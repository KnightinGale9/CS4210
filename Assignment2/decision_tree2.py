# -------------------------------------------------------------------------
# AUTHOR: Zhong Ooi
# FILENAME: decision_tree2.py
# SPECIFICATION: finding the accuracy of decision tree models created from different datasets
#                and then test each model accuracy through a constant testing dataset
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour 30 min
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv',
            'contact_lens_training_3.csv']
for ds in dataSets:
    dbTraining = []
    X = []
    Y = []
    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)
    # transform the original categorical training features to numbers and add to the
    # 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # transform the original categorical training classes to numbers and add to the
    # vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

    #all the feature values found in each attribute and the class values
    feature_values = {0: {'Young': 1, 'Prepresbyopic': 2, 'Presbyopic': 3}, 1: {'Myope': 1, 'Hypermetrope': 2},
                      2: {'Yes': 1, 'No': 2}, 3: {'Reduced': 1, 'Normal': 2}, 4: {'Yes': 1, 'No': 2}}
    temp = []
    for instance in dbTraining:
        for i, value in enumerate(instance):  # retriving the feature values
            # using feature_values to get the number values and adding to a list
            temp.append(feature_values[i][value])
        # adding to vector X
        X.append(temp[:len(instance) - 1].copy())
        # adding to Vector Y
        Y.append(temp[len(instance) - 1])
        # clear temp to be used again
        temp.clear()

    # fitting the decision tree to the data
    # print(X)
    # print(Y)
    #store the 10 test runs
    accuracy = []
    # loop your training and test tasks 10 times here
    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)
        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =
        dbTest = []

        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)
        correct_prediction = 0
        for data in dbTest:
            XTest = []
            YTest = 0;
            # transform the features of the test instances to numbers following the
            # same strategy done during training,
            for j, value in enumerate(data):  # retriving the feature values
                # using conversion to get the number values and adding to a list
                temp.append(feature_values[j][value])
            # print(temp)
            # adding to vector X
            XTest.append(temp[:len(instance) - 1].copy())
            # adding to Vector Y
            YTest = (temp[len(instance) - 1])
            # clear temp to be used again
            temp.clear()
            # and then use the decision tree to make the class prediction. For
            # instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            class_predicted = clf.predict(XTest)[0]
            # compare the prediction with the true label (located at data[4]) of the
            # test instance to start calculating the accuracy.
            # --> add your Python code here
            if class_predicted == YTest:
                correct_prediction += 1
        # find the lowest accuracy of this model during the 10 runs (training and
        # test set)
        # --> add your Python code here
        accuracy.append(correct_prediction)
    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    print("final accuracy when training on",ds,":",min(accuracy)/len(dbTest))





