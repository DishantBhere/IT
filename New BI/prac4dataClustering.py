#Data Clustering using Python (K-Means)

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


data = load_iris()
X = data.data


kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)


labels = kmeans.labels_


plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red', marker='X', s=200)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()
