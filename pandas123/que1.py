# Create a DataFrame with columns: Product, Price, and Quantity.
# Add a new column Total (Price * Quantity).
# Save the resulting DataFrame to a CSV file.

import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "headphones", "airpods"],
    "Price": [86000, 75000, 2500, 4500],
    "Quantity": [1, 3, 5, 6]
}

df = pd.DataFrame(data)
 
# to add a new column 
df["Total"] = df["Price"] * df["Quantity"] 
print("\nThe total price is :")
print(df)

#saving it in a csv file 
df.to_csv("Total.csv", index = False)
print("\nData saved Total.csv")
