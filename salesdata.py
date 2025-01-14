import csv 
file_path = "sales_data.csv"

def create_csv():
    headers = ["product", "region", "sales", "price", "total"]
    with open(file_path, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("sales data created")

    """
    if product in sales_revenue:
    sales_revenue[product] = product + revenue
    else:
    sales_revenue[product] = revenue 
    sales * price 
    """

def add_sale(product, region, sales, price, total):
   total = sales * price
   with open(file_path, mode = "a", newline ="") as file:
    writer = csv.writer(file)
    writer.writerow([product , region, sales, price, total])
    print("sale data added")
    
# calculate the total sales revenue 
def calculate_sales_revenue():
    sales_revenue = 0 
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_revenue += float(row["total"])
        print(f"total sales revenue: ${sales_revenue:.2F}")


create_csv()
add_sale("laptop", "kathmandu", 2, 1200.50, 2401)
add_sale("iphone", "pokara", 1, 10000, 10000)
add_sale("bottle", " kathmandu", 5, 1500, 7500)
add_sale("mouse", "kathmandu", 3, 500, 1500)
add_sale("monitor", "pokhara", 2, 9000, 18000)

calculate_sales_revenue()

 # using  numpy calculate the avrage revenue for all products 
import numpy as np 
