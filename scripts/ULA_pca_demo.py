import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/pca-demo.csv', index_col=0)

# Convert to a NumPy matrix and transpose it like Sage's A = matrix(...).T
A = df.values.T  # shape will be (3, n)

# Equivalent to the pca_plot function (2D scatter of columns)
def pca_plot(A):
    # Each column of A is a 3D point, so we transpose to get rows as points
    data_points = A.T  # shape becomes (n, 3)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(data_points[:, 0], data_points[:, 1], data_points[:, 2])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_box_aspect([1, 1, 1])  # aspect_ratio=1
    plt.tight_layout()
    plt.show()

pca_plot(A)
