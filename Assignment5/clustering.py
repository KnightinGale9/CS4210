# -------------------------------------------------------------------------
# AUTHOR: Zhong Ooi
# FILENAME: clustering.py
# SPECIFICATION: A program to find the best number of clusters to solve this KMeans problems
# FOR: CS 4210- Assignment #5
# TIME SPENT: 1 hr 30 min
# -----------------------------------------------------------*/

# importing some Python libraries
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn import metrics

df = pd.read_csv('training_data.csv', sep=',', header=None)  # reading the data by using Pandas library
# print(df)
# assign your training data to X_training feature matrix
X_training = np.array(df.values)
scores = [[], []]
# run kmeans testing different k values from 2 until 20 clusters
# Use:  kmeans = KMeans(n_clusters=k, random_state=0)
#      kmeans.fit(X_training)
# --> add your Python code
for k in range(2, 21):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_training)
    scores[0].append(silhouette_score(X_training, kmeans.labels_))
    kmeans2 = AgglomerativeClustering(n_clusters=k)
    kmeans2.fit(X_training)
    scores[1].append(silhouette_score(X_training, kmeans.labels_))

    # for each k, calculate the silhouette_coefficient by using: silhouette_score(X_training, kmeans.labels_)
    # find which k maximizes the silhouette_coefficient
    # --> add your Python code here

# plot the value of the silhouette_coefficient for each k value of kmeans so that we can see the best k
# --> add your Python code here
print("Best KMeans of Cluster:", 2+scores[0].index(max(scores[0])))
print("Best AgglomerativeClustering of Cluster:", 2+scores[1].index(max(scores[1])))
plt.plot(scores[0], label="KMeans")
plt.xticks(np.arange(0, 20, step=1))
plt.legend()
plt.show()
plt.plot(scores[1], label="AgglomerativeClustering")
plt.xticks(np.arange(0, 20, step=1))
plt.legend()
plt.show()
# reading the test data (clusters) by using Pandas library
# --> add your Python code here
df = pd.read_csv('testing_data.csv', sep=',', header=None)
# assign your data labels to vector labels (you might need to reshape the row vector to a column vector)
# do this: np.array(df.values).reshape(1,<number of samples>)[0]
# --> add your Python code here
X_test = np.array(df.values).reshape(1, len(df))[0]
# Calculate and print the Homogeneity of this kmeans clustering
# print("K-Means Homogeneity Score = " + metrics.homogeneity_score(labels, kmeans.labels_).__str__())
# --> add your Python code here
print("K-Means Homogeneity Score = " + metrics.homogeneity_score(X_test, kmeans.labels_).__str__())
print("AgglomerativeClustering Homogeneity Score = " + metrics.homogeneity_score(X_test, kmeans2.labels_).__str__())