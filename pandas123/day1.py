import pandas as pd 

# create a DataFram from a dictionary 
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("Dataframe:")
print(df)

# Read data from a CSV file 
# (Assume 'data.csv' exists in the current directory)
# df = pd.read_csv("data.csv")

#Display the first few rows of dataframe 
print("\nFirst 2 rows:")
print(df.head(2))

# Filter rows where Age > 25 
filtered_df = df[df["Age"] > 25]
print("\nfiltered DataFrame:")
print(filtered_df)

# Add a new column 
df["Score"] = [80, 90, 88]
print("\nDataFrame with new column:")
print(df)

# Save the Dataframe to a CSV file 
df.to_csv("Output.csv", index = False)
print("\nData saved to output.csv")

# for calculations 
df["Total"] = df["Price"] * df["Quantity"] 
print("\nThe total price is :")
print(df)