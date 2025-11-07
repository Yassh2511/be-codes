# Program: Agglomerative Hierarchical Clustering

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 1: Load Dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Sample Data:")
print(data.head())

# Step 2: Data Normalization (important for clustering)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Create Linkage Matrix for Dendrogram
linked = linkage(scaled_data, method='ward')

# Step 4: Plot Dendrogram
plt.figure(figsize=(8, 6))
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=True)
plt.title("Dendrogram - Hierarchical Clustering (Iris Dataset)")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.xticks([])
plt.show()

# Step 5: Apply Agglomerative Clustering
# (Let’s assume we want 3 clusters for the Iris dataset)
cluster = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
labels = cluster.fit_predict(scaled_data)

# Step 6: Add cluster labels to DataFrame
data['Cluster'] = labels

print("\nClustered Data Sample:")
print(data.head())

# Step 7: Visualize the Clusters (2D Plot using first two features)
plt.figure(figsize=(8, 6))
plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=labels, cmap='rainbow')
plt.title("Agglomerative Hierarchical Clustering (3 Clusters)")
plt.xlabel("Feature 1 (sepal length)")
plt.ylabel("Feature 2 (sepal width)")
plt.show()
