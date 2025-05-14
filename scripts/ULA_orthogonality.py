import numpy as np
import pandas as pd
import sympy
import matplotlib.pyplot as plt

# Projection of vector b onto the subspace spanned by the list 'basis'
def projection(b, basis):
    if len(basis) == 0:
        return sympy.Matrix([0] * len(b))
    return sum((b.dot(v) / v.dot(v)) * v for v in basis)

# Normalize a vector
def unit(v):
    return v / v.norm()

# Gram-Schmidt orthonormalization
def gs(basis):
    onbasis = []
    for b in basis:
        proj = projection(b, onbasis)
        u = unit(b - proj)
        onbasis.append(u)
    return onbasis

# QR Decomposition
def QR(A):
    A_sym = [sympy.Matrix(A[:, i]) for i in range(A.shape[1])]
    Q_columns = gs(A_sym)
    Q = sympy.Matrix.hstack(*Q_columns)
    R = Q.T * sympy.Matrix(A)
    return Q, R

# Vector of ones
def onesvec(n):
    return sympy.Matrix([1] * n)

# Demean a vector
def demean(v):
    return v - sympy.Rational(sum(v), len(v)) * onesvec(len(v))

# Construct a Vandermonde matrix
def vandermonde(data, k):
    rows = [[datum**j for j in range(k + 1)] for datum in data]
    return sympy.Matrix(rows)

# Plot data and polynomial model
def plot_model(xhat, data, domain=None):
    x = sympy.Symbol('x')
    k = len(xhat) - 1

    # Extract domain from data if not provided
    xs = [d[0] for d in data]
    xmin, xmax = min(xs), max(xs)
    if domain is None:
        domain = (xmin, xmax)

    # Create the polynomial expression
    poly_expr = sum(xhat[j] * x**j for j in range(k + 1))
    f_lambdified = sympy.lambdify(x, poly_expr, modules=['numpy'])

    # Plot
    xs_plot = np.linspace(domain[0], domain[1], 200)
    ys_plot = f_lambdified(xs_plot)

    data = np.array(data)
    plt.figure(figsize=(6, 4))
    plt.scatter(data[:, 0], data[:, 1], color='blue', s=40, label='Data')
    plt.plot(xs_plot, ys_plot, color='red', label='Model')
    plt.legend()
    plt.grid(True)
    plt.show()
