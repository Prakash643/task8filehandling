# File Handling using TXT file

try:
    # 1. Write data to file
    file = open("data.txt", "w")
    file.write("Name: Prakash\n")
    file.write("Role: Python Intern\n")
    file.write("Email: prakash@gmail.com\n")
    file.close()

    # 2. Read file contents
    file = open("data.txt", "r")
    print("Reading file content:")
    print(file.read())
    file.close()

    # 3. Append data to file
    file = open("data.txt", "a")
    file.write("Location: India\n")
    file.close()

    # 4. Read after appending
    file = open("data.txt", "r")
    print("\nAfter appending:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found error!")
except Exception as e:
    print("Error:", e)
