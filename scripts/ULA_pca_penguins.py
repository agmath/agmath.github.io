import pandas as pd
import sympy as sp
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/penguins.csv')
df = df.drop(columns=['Unnamed: 0'])

data = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/penguins_data.csv')
data = data.drop(columns=['Unnamed: 0'])

# Convert to sympy Matrix and mean center
data_matrix = sp.Matrix(data.values.tolist())
n_rows = data_matrix.rows

# Compute column means and center data
data_mean = sp.Matrix([sum(data_matrix.col(i)) / n_rows for i in range(data_matrix.cols)])
centered_data = data_matrix.rowwise_subtract(data_mean.T)

# Transpose to match A = matrix(...).T in Sage
A = centered_data.T  # Shape: 4 x N

# Compute covariance matrix and diagonalize
def covariance_matrix(M):
    n = M.cols
    return (1 / n) * (M @ M.T)

cov = covariance_matrix(A)
eigenvals, eigenvecs = cov.diagonalize()

# Select top two principal components
evals_and_evecs = sorted(
    zip(eigenvals.diagonal(), eigenvecs.columns()),
    key=lambda x: abs(x[0]),
    reverse=True
)
V = sp.Matrix.hstack(*[vec for val, vec in evals_and_evecs[:2]])  # 4 x 2

# Project data into 2D and convert entries to floats
M_projected = (V.T @ A).T.tolist()
M_projected = [[float(entry) for entry in row] for row in M_projected]

# Put projections in a DataFrame
proj = pd.DataFrame(M_projected, columns=[0, 1])
proj['Species'] = df['Species']
proj['Sex'] = df['Sex']

# Plot original culmen data
def culmen_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect(1)
    sns.scatterplot(
        x='Culmen Length (mm)',
        y='Culmen Depth (mm)',
        hue='Species',
        style='Sex',
        data=df, ax=ax
    )
    plt.legend(bbox_to_anchor=(0, 1.05), loc=3, borderaxespad=0.)
    plt.show()

# PCA scatterplot by sex
def pca_plot(sex='all'):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect(1)
    subset = proj
    if sex == 'male':
        subset = proj[proj['Sex'] == 'Male']
        sns.scatterplot(x=0, y=1, hue='Species', data=subset, ax=ax)
    elif sex == 'female':
        subset = proj[proj['Sex'] == 'Female']
        sns.scatterplot(x=0, y=1, hue='Species', data=subset, ax=ax)
    else:
        sns.scatterplot(x=0, y=1, hue='Species', style='Sex', data=subset, ax=ax)
    plt.legend(bbox_to_anchor=(-.15, 1.05), loc=2, borderaxespad=0.)
    plt.show()

# Usage
culmen_plot()
pca_plot()      # Try: pca_plot('male') or pca_plot('female')
