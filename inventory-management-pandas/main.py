import pandas as pd

inventory = pd.read_csv("inventory.csv")

# Filter example
seed_request = inventory.loc[
    (inventory["location"] == "Brooklyn") &
    (inventory["product_type"] == "seeds")
]

# Stock status
inventory["in_stock"] = inventory["quantity"] > 0

# Total value
inventory["total_value"] = inventory["price"] * inventory["quantity"]

# Full description
inventory["full_description"] = inventory.apply(
    lambda row: f"{row.product_type} - {row.product_description}",
    axis=1
)

print(inventory.head())
