# Task 2: Demonstrate List Slicing 


numb = list(range(1, 11))  # list of numbers from 1 to 10

first_five = numb[:5] #Extracts the first five elements from the list.

reversed_list = list(reversed(first_five)) #Reverses these extracted elements.

# output
print(f"Original List: {numb}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reversed_list}")
