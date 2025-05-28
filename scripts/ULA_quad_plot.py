import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables
r, theta = sp.symbols('r theta')

# Define symbolic vector in polar coordinates
v = sp.Matrix([r * sp.cos(theta), r * sp.sin(theta)])

# Define symmetric matrix A symbolically
A = sp.Matrix([[2, 1], [1, 3]])

def quad_plot(A):
    # Define the quadratic form q(r, theta) = v^T * A * v
    q_expr = (v.T * A * v)[0]

    # Convert to a numerical function using lambdify
    q_func = sp.lambdify((r, theta), q_expr, modules='numpy')
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define grid in polar coordinates
    r_vals = np.linspace(0, 2, 100)
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    R, Theta = np.meshgrid(r_vals, theta_vals)

    # Compute X, Y from polar coordinates
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    # Evaluate Z using the lambdified function
    Z = q_func(R, Theta)

    # Plot surface
    ax.plot_surface(X, Y, Z, color='orange', alpha=0.9, rstride=1, cstride=1, edgecolor='none')

    # Add parametric curve on unit circle
    t_vals = np.linspace(0, 2 * np.pi, 300)
    x_curve = np.cos(t_vals)
    y_curve = np.sin(t_vals)
    z_curve = q_func(1, t_vals)
    ax.plot(x_curve, y_curve, z_curve, color='black', linewidth=2)

    # Formatting
    ax.set_box_aspect([1, 1, 0.5])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("q(x) = xᵀAx")
    plt.tight_layout()
    plt.show()
