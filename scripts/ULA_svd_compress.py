import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# --- Display image from matrix ---
def display_image(matrix):
    matrix = np.array(matrix)
    matrix = np.clip(matrix, 0, 255)
    return Image.fromarray(matrix.astype('uint8'))

# --- Low-rank SVD approximation ---
def approximate(A, k):
    A = np.array(A, dtype=float)
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    r = min(k, len(s))
    u_k = u[:, :r]
    s_k = np.diag(s[:r])
    vh_k = vh[:r, :]
    return u_k @ s_k @ vh_k

# --- Display matrix as grid of colored squares ---
def display_matrix(A):
    A = np.array(A)
    A = A / np.max(np.abs(A))  # Normalize
    nrows, ncols = A.shape
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i in range(nrows):
        for j in range(ncols):
            val = A[i, j]
            if val > 1: val = 1
            if val < -1: val = -1
            if val >= 0:
                fill = (val, val, val)
            else:
                fill = (-val, 0, 0)
            stroke = tuple(1 - x for x in fill)
            rect = plt.Rectangle((j, nrows - i - 1), 1, 1, facecolor=fill, edgecolor=stroke)
            ax.add_patch(rect)
    
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    plt.gca().invert_yaxis()
    plt.show()

# --- Display vector as matrix plot ---
def display_vector(v):
    v = np.array(v)
    v = v / np.max(np.abs(v))
    return display_matrix(v.reshape(-1, 1))

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

# --- Load image into matrix ---
def load_grayscale_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert('LA')
    return np.array(image)[:, :, 0]

# --- Load CSV into numpy array ---
def load_csv_matrix(url, sep=None):
    df = pd.read_csv(url, header=None, sep=sep)
    return df.values

# --- Load assets ---
image = load_grayscale_image('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/utah-gray.png')
noise = load_csv_matrix('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/noise.csv')
letter = load_csv_matrix('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/letter.csv', sep=' ')
noiseimage = load_grayscale_image('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/new-utah-noise.png')

# --- Example usage ---
# Approximate and display an image
approx_image = approximate(image, k=50)
display_image(approx_image).show()

# Display matrix structure
display_matrix(letter)

# Plot singular values of a matrix
plot_sv(letter)
