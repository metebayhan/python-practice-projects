from math import sqrt
import numpy as np

def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)

returns_asset_a = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_asset_b = [-0.13, -0.15, 0.31, -0.06, -0.29]

def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0

    for x in dataset:
        numerator += (x - mean) ** 2

    return numerator / len(dataset)

def calculate_stddev(dataset):
    return sqrt(calculate_variance(dataset))

# NumPy results (for comparison)
numpy_std_a = np.std(returns_asset_a)
numpy_std_b = np.std(returns_asset_b)

# Custom implementation
stddev_a = calculate_stddev(returns_asset_a)
stddev_b = calculate_stddev(returns_asset_b)

print("Standard deviation (custom) Asset A:", display_as_percentage(stddev_a))
print("Standard deviation (custom) Asset B:", display_as_percentage(stddev_b))

print("Standard deviation (NumPy) Asset A:", display_as_percentage(numpy_std_a))
print("Standard deviation (NumPy) Asset B:", display_as_percentage(numpy_std_b))

if stddev_a > stddev_b:
    print("Asset A is riskier.")
else:
    print("Asset B is riskier.")
