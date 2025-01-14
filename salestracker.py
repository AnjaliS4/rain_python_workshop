import csv
# file path for the sales tracker 
file_path = "sales_tracker.csv"

#create a new CSV file with headers 
def create_csv():
    headers = ["Dates", "product", "Quantity", "Price per unit", "Total"]
    with open(file_path, mode ="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("sales tracker created")
# add a new sale record to the CSV file 
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode = "a", newline ="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("sale record added")

# calculate total sales from the CSV file 
def calculate_total_sales():
    total_sales = 0 
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
        print(f"Total sales: ${total_sales:.2F}")

#example usuage 
create_csv()
add_sale("2025-01-06", "Laptop", 2, 1200.50)
add_sale("2025-01-06", "Mouse", 5, 25.99)
calculate_total_sales()