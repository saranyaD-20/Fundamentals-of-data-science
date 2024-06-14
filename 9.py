import numpy as np

# Assuming student_scores is your NumPy array containing student scores
student_scores = np.array([
    [85, 90, 88, 92],  # Math scores
    [78, 85, 80, 88],  # Science scores
    [90, 92, 85, 89],  # English scores
    [88, 85, 90, 86]   # History scores
])

# Calculate the average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Identify the subject with the highest average score
highest_average_score_subject = np.argmax(average_scores)

# Printing the results
print("Average score for each subject:", average_scores)
print("Subject with the highest average score:", highest_average_score_subject)
