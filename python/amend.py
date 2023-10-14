# Write a program that amend the Q2 and counts the number of student in it. Print
# the student count at the end of the program.

# Open the file in read mode ('r') and read the content
with open("studentlist.txt", "r") as file:
    content = file.read()

# Display the content on the screen
print("Content of studentlist.txt:")
print(content)

# Count the number of students by splitting the content into lines
lines = content.split("\n")
student_count = len([line for line in lines if line.strip()])

print(f"Number of students: {student_count}")
