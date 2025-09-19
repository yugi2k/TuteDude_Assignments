
# Task 1: Read a File and Handle Errors 

try:    
    with open("sample.txt", "r") as file:       # Open the file
        
        for line_no, line in enumerate(file, start=1):
            print(f"Line {line_no}: {line}")   # print line by line with no.
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.") # error handling





