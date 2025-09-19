# Task 2: Write and Append Data to a File

# 1- Takes user input and writes it to a file named output.txt.
user_text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:   
    file.write(user_text + "\n")

print("Data successfully written to output.txt.")

#Append data
extra_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:   
    file.write(extra_text + "\n")

print("Data successfully appended.")

# output
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:   
    for line_no, line in enumerate(file, start=1):
        print(f"Line {line_no}: {line}")

