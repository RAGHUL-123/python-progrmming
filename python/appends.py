# Write a program to prompts user for a new name and appends it to an existing text
# file.

# Prompt the user for a new name
new_name = input("Enter a new name to append to the file: ")

# Open the file in append mode ('a') and write the new name
with open("studentlist.txt", "a") as file:
    file.write(new_name + "\n")

print(f"{new_name} has been appended to studentlist.txt.")
