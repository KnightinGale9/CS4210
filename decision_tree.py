# -------------------------------------------------------------------------
# AUTHOR: Zhong Ooi
# FILENAME: decision_tree.py
# SPECIFICATION: A program to convert a dataset table into numbers to
#                be able to interact with a prebuilt decision_tree graph.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 4 hours
# -----------------------------------------------------------*/
# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
# AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []
# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features to numbers and add to the 4D
# array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# transform the original categorical training classes to numbers and add to the
# vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# creating a dictionary of sets to store all possible feature values at each position
conversion = {}
for i in range(len(db[0])):
    conversion[i] = set()
# scrub through all values of db and find all unique values
for instance in db:
    for i in range(len(instance)):
        conversion[i].add(instance[i])
# convert the set into a dictionary so we can get constant time access to feature values
temp = {}
for key in conversion:
    # convert to list so we prepare it for conversion
    conversion[key] = list(conversion[key])
    # since the structure was a set first need to sort it to keep the graphs consitant and to keep yes as 1 and no as 2
    conversion[key].sort(reverse=True)
    # remake the list as a dictionary with proper numbers
    for i, value in enumerate(conversion[key]):
        temp.update({value: i + 1})
    # change the dictionary of sets to a dictionary of dictionary
    conversion[key] = temp.copy()
    # clear temp
    temp.clear()
# outputs what each feature value at each position is mapped to
print("feature:value")
for feature in conversion:
    print(f"{' ' * 6}{feature}:{conversion[feature]}")
print()
# With the dictionary of dictionary classifying all the possible feature values start going through the db and
# converting each line to numbers add adding it to X and Y
temp = []
for instance in db:
    for i, value in enumerate(instance):  # retriving the feature values
        # using conversion to get the number values and adding to a list
        temp.append(conversion[i][value])
    # print(temp)
    # adding to vector X
    X.append(temp[:len(instance) - 1].copy())
    # adding to Vector Y
    Y.append(temp[len(instance) - 1])
    # clear temp to be used again
    temp.clear()

# fitting the decision tree to the data
print(X)
print(Y)
clf = tree.DecisionTreeClassifier(criterion='entropy', )
clf = clf.fit(X, Y)
# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'],
               class_names=['Yes', 'No'], filled=True, rounded=True)
plt.show()
