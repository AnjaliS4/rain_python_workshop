
import csv
import openpyxl
import random


student_score_file = "student_scores.csv"
file_path = "results.xlsx"
def create_csv():
    """creates a csv file with headers"""
    headers = [ "name", "subject","score"]
    with open(student_score_file, mode="w", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(headers)
def add_student(name, subject, score):
    with open(student_score_file , mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,subject, score])
    print("students record added")
def calculate_total_score():
    total_score  = 0
    with open(student_score_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["total"])
    print(f"total score: ${total_score:.2f}")




#example usage

def generate_random_students_data(num_records):
    names = ["Alice", "Bob", "Charlie"]
    subjects = ["maths","science"]
    score = [90, 95]
    
    for _ in range(num_records):
        name = random.choice(names)
        subject = random.choice(subjects)
        score = random.randint(0, 100)


calculate_sales_revenue()

    print(f"Generated {num_records} random students data.")
    
        
create_csv()
generate_random_students_data(3)

################################

# csv_content = """  name, subject, score
# Alice, Math, 85 
# Bob, Math, 90
# Alice, Science, 95
# Bob, Science, 80
# Charlie, Math, 70
# Charlie, Science, 75

# """
create_csv()
add_sale("laptop", "kathmandu", 2, 1200.50, 2401)
add_sale("iphone", "pokara", 1, 10000, 10000) 
add_sale("bottle", " kathmandu", 5, 1500, 7500)
add_sale("mouse", "kathmandu", 3, 500, 1500)
add_sale("monitor", "pokhara", 2, 9000, 18000)





