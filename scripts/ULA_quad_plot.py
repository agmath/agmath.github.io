import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define your matrix A (as a NumPy array)
A = np.array([[3, 1],
              [1, 2]])

def q(r, theta):
    v = np.array([r * np.cos(theta), r * np.sin(theta)])
    return v @ A @ v  # quadratic form: v^T * A * v

def quad_plot(A):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define grid in polar coordinates
    r_vals = np.linspace(0, 2, 100)
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    R, Theta = np.meshgrid(r_vals, theta_vals)

    # Compute X, Y from polar coordinates
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    # Compute Z = q(r, theta)
    Z = np.vectorize(q)(R, Theta)

    # Plot surface
    ax.plot_surface(X, Y, Z, color='orange', alpha=0.9, rstride=1, cstride=1, edgecolor='none')

    # Add parametric curve on unit circle
    t_vals = np.linspace(0, 2 * np.pi, 300)
    x_curve = np.cos(t_vals)
    y_curve = np.sin(t_vals)
    z_curve = np.array([q(1, t) for t in t_vals])
    ax.plot(x_curve, y_curve, z_curve, color='black', linewidth=2)

    # Formatting
    ax.set_box_aspect([1, 1, 0.5])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("q(x) = xᵀAx")
    plt.tight_layout()
    plt.show()

quad_plot(A)
