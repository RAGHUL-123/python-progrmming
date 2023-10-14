# List of tuples containing student names and their scores in three subjects
student_scores = [
    ("Alice", (90, 85, 88)),
    ("Bob", (78, 92, 95)),
    ("Charlie", (85, 88, 92)),
    ("David", (92, 78, 86)),
]

# Initialize an empty dictionary to store the average scores
average_scores = {}

# Calculate the average score for each student and store in the dictionary
for student, scores in student_scores:
    average_score = sum(scores) / len(scores)
    average_scores[student] = average_score

# Display the average scores for each student
for student, average_score in average_scores.items():
    print(f"{student}: Average Score = {average_score:.2f}")
