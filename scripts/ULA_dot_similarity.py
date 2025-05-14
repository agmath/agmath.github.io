import pandas as pd
import numpy as np
import sympy
import matplotlib.pyplot as plt

# Use sympy's pi and N for symbolic-to-float conversion
pi = sympy.pi
def degrees(x):
    return float(sympy.N(x * 180.0 / pi))

def demean(v):
    mean_val = np.mean(v)
    return v - mean_val

def series_plot(v, color):
    plt.plot(v, color=color)
    plt.scatter(range(len(v)), v, color=color, s=20)
    plt.show()

# Load the data
events = pd.read_csv("https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/events.csv", index_col=0)
series = pd.read_csv("https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/time-series.csv", header=None)

# Convert specific columns to sympy vectors
veterans = sympy.Vector(events['Veterans Day'].values)
memorial = sympy.Vector(events['Memorial Day'].values)
labor = sympy.Vector(events['Labor Day'].values)
golden = sympy.Vector(events['Golden Globe Awards'].values)
superbowl = sympy.Vector(events['Super Bowl'].values)

# Series vectors
s1 = sympy.Vector(series.iloc[:, 0].values)
s2 = sympy.Vector(series.iloc[:, 3].values)
s3 = sympy.Vector(series.iloc[:, 1].values)
s4 = sympy.Vector(series.iloc[:, 2].values)
