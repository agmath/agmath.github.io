import pandas as pd
import sympy as sp
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/iris.data')

# Extract numeric part
data = df[df.columns[:4]]

# Convert to sympy Matrix and center
data_matrix = sp.Matrix(data.values.tolist())
data_mean = sp.Matrix([[sum(data_matrix.col(i)) / data_matrix.rows for i in range(data_matrix.cols)]])

# Repeat the row to create a 150x4 matrix (same shape as data_matrix)
mean_matrix = sp.Matrix([data_mean.tolist()[0]] * data_matrix.rows)

# Subtract element-wise
centered_data = data_matrix - mean_matrix



# Transpose to match original A = matrix(...).T in Sage
A = centered_data.T  # shape: 4 x 150

# Plot original sepal data
def sepal_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect(1)
    sns.scatterplot(
        x='sepal length', y='sepal width',
        hue='species', style='species',
        data=df, ax=ax
    )
    plt.legend(bbox_to_anchor=(0, 1.05), loc=3, borderaxespad=0.)
    plt.show()

# Compute covariance matrix (symbolically)
def covariance_matrix(M):
    n = M.cols
    return (1 / n) * (M @ M.T)

# Eigen decomposition with sympy
cov = covariance_matrix(A)
eigenvals, eigenvecs = cov.diagonalize()

# Sort eigenvectors by decreasing eigenvalue magnitude
evals_and_evecs = sorted(
    zip(eigenvals.diagonal(), eigenvecs.T.tolist()),
    key=lambda x: abs(x[0]),
    reverse=True
)
top2_vectors = [sp.Matrix(vec) for val, vec in evals_and_evecs[:2]]
V = sp.Matrix.hstack(*top2_vectors)


# Project data into 2D
M_projected = (V.T @ A).T.tolist()  # shape: 150 x 2

# Convert to DataFrame for plotting
proj = pd.DataFrame(M_projected, columns=[0, 1])
proj['species'] = df['species']

def pca_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect(1)
    sns.scatterplot(x=0, y=1, hue='species', style='species', data=proj, ax=ax)
    plt.legend(bbox_to_anchor=(0, 1.05), loc=3, borderaxespad=0.)
    plt.show()

# Run plots
sepal_plot()
pca_plot()
