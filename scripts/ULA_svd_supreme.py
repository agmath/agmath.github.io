import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

# --- Display a column of a matrix ---
def display_column(A, k):
    A = np.array(A)
    col = A[:, k]
    col = col / np.max(np.abs(col))
    return display_matrix(col.reshape(-1, 1))

# --- Display matrix using colored squares ---
def display_matrix(A):
    A = np.array(A, dtype=float)
    max_val = np.max(A)
    min_val = np.min(A)
    scale = max(abs(max_val), abs(min_val))
    A_scaled = A / scale

    nrows, ncols = A.shape
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    for i in range(nrows):
        for j in range(ncols):
            val = A_scaled[i, j]
            if val > 1: val = 1
            if val < -1: val = -1
            if val >= 0:
                fill = (val, val, val)
            else:
                fill = (-val, 0, 0)
            stroke = tuple(1 - c for c in fill)
            rect = plt.Rectangle((j, nrows - i - 1), 1, 1, facecolor=fill, edgecolor=stroke)
            ax.add_patch(rect)

    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    plt.gca().invert_yaxis()
    plt.show()

# --- Plot singular values ---
def plot_sv(A):
    A = np.array(A, dtype=float)
    sv = np.linalg.svd(A, compute_uv=False)
    plt.plot(sv, '-o')
    plt.title("Singular Values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

# --- Outer product u*v^T ---
def outer(u, v):
    u = np.array(u).reshape(-1, 1)
    v = np.array(v).reshape(1, -1)
    return u @ v

# --- Low-rank SVD approximation ---
def approximate(A, k):
    A = np.array(A, dtype=float)
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    r = min(k, len(s))
    u_k = u[:, :r]
    s_k = np.diag(s[:r])
    vh_k = vh[:r, :]
    return u_k @ s_k @ vh_k

# --- Load datasets ---
cases = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/Rehnquist-cases.csv', index_col=0)
fivefour = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/Rehnquist-five-four.csv', index_col=0)
agreement = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/rehnquist-agreement.csv', index_col=0)

# --- Example usage ---
# display_column(agreement.values, 0)
# display_matrix(agreement.values)
# plot_sv(agreement.values)
# approx = approximate(agreement.values, 2)
# display_matrix(approx)
