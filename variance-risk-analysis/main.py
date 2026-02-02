import numpy as np

returns_asset_a = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_asset_b = [-0.13, -0.15, 0.31, -0.06, -0.29]

variance_asset_a = np.var(returns_asset_a)
variance_asset_b = np.var(returns_asset_b)

def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0

    for x in dataset:
        numerator += (x - mean) ** 2

    return numerator / len(dataset)

variance_asset_a = calculate_variance(returns_asset_a)
variance_asset_b = calculate_variance(returns_asset_b)

print('The variance of Asset A returns is', variance_asset_a)
print('The variance of Asset B returns is', variance_asset_b)

if variance_asset_a > variance_asset_b:
    print("Asset A is riskier.")
else:
    print("Asset B is riskier.")
