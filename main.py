# Function to append the second list to the first list
def append_lists(list1, list2):
    if isinstance(list2, int):  # Check if the second input is a single number
        list1.append(list2)
    elif isinstance(list2, list):  # Check if the second input is a list of numbers
        list1.extend(list2)

# Input two lists from the user
list1 = []
list2 = input("Enter the second list (single number or list of numbers separated by spaces): ").split()

# Convert the elements of list2 to integers
list2 = [int(x) for x in list2]

# Call the function to append list2 to list1
append_lists(list1, list2)

# Display the combined list
print("Combined list:", list1)
