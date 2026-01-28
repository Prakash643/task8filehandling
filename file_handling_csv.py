# File Handling using CSV file

import csv

# 1. Write data to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Role", "Department"])
    writer.writerow([1, "Ravi", "Intern", "Python"])
    writer.writerow([2, "Sita", "Intern", "Data Science"])
    writer.writerow([3, "Amit", "Intern", "Web Development"])

print("CSV file written successfully.")

# 2. Read CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("\nReading CSV file:")
    for row in reader:
        print(row)
