import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/clusters_data.csv", header=None)
data = df.values

# K-means implementation
def kmeans(data, k):
    N = 15  # Number of iterations
    centroid_indices = np.random.choice(len(data), size=k, replace=False)
    centroids = data[centroid_indices]
    for _ in range(N):
        clusters = [[] for _ in range(k)]
        for datum in data:
            distances = [np.linalg.norm(datum - centroids[j]) for j in range(k)]
            clusters[np.argmin(distances)].append(datum)
        clusters = [np.array(cluster) for cluster in clusters]
        centroids = [np.mean(cluster, axis=0) if len(cluster) > 0 else centroids[j]
                     for j, cluster in enumerate(clusters)]
        centroids = np.array(centroids)
    distances = [
        sum(np.linalg.norm(point - centroids[i]) ** 2 for point in clusters[i])
        for i in range(k)
    ]
    return [clusters, centroids, sum(distances) / len(data)]

# Run k-means multiple times and keep the best (lowest objective)
def minimalobjective(data, k):
    results = [kmeans(data, k) for _ in range(10)]
    results = sorted(results, key=itemgetter(2))
    return results[0]

# Plot the clusters
def plotclusters(clusters, centroids):
    k = len(clusters)
    cmap = get_cmap('rainbow')
    colors = [cmap(i / k) for i in range(k)]

    plt.figure(figsize=(6, 6))
    for i in range(k):
        cluster = np.array(clusters[i])
        if len(cluster) > 0:
            plt.scatter(cluster[:, 0], cluster[:, 1], s=20, color=colors[i], label=f"Cluster {i+1}")
    centroids = np.array(centroids)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=50, c='black', marker='x', label='Centroids')
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()
