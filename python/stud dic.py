# Create a dictionary of student names and a corresponding tuple of their exam
# scores. Write a program to find and display the name of the student with the highest
# score.
#
# Create a dictionary of student names and their exam scores

student_scores = {
    "Alice": (90, 85, 88),
    "Bob": (78, 92, 95),
    "Charlie": (85, 88, 92),
    "David": (92, 78, 86),
}

# Function to find the student with the highest score
def find_student_with_highest_score(scores_dict):
    if not scores_dict:
        return None

    highest_score = -1
    highest_scoring_student = None

    for student, scores in scores_dict.items():
        average_score = sum(scores) / len(scores)
        if average_score > highest_score:
            highest_score = average_score
            highest_scoring_student = student

    return highest_scoring_student

# Find and display the name of the student with the highest score
highest_scorer = find_student_with_highest_score(student_scores)

if highest_scorer:
    print(f"The student with the highest score is {highest_scorer}.")
else:
    print("No students in the dictionary.")
