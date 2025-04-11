import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load mentor data
mentors_df = pd.read_csv("mentors.csv")

print("Welcome to the Mentor Recommendation System")

# Ask for student name
name = input("Enter your name: ")

# MCQ for subject
subjects = ["Legal Reasoning", "Logical Reasoning", "English", "GK", "Quantitative Techniques"]
print("\nSelect your preferred subject:")
for i, s in enumerate(subjects):
    print(f"{i+1}. {s}")
subject_choice = subjects[int(input("Enter option number: ")) - 1]

# MCQ for college
colleges = ["NLSIU Bangalore", "NLU Delhi", "NLU Jodhpur", "NLU Patna", "NLU Bhopal"]
print("\nSelect your target college:")
for i, c in enumerate(colleges):
    print(f"{i+1}. {c}")
college_choice = colleges[int(input("Enter option number: ")) - 1]

# MCQ for preparation level
levels = ["Beginner", "Intermediate", "Advanced"]
print("\nSelect your current preparation level:")
for i, l in enumerate(levels):
    print(f"{i+1}. {l}")
level_choice = levels[int(input("Enter option number: ")) - 1]

# MCQ for learning style
styles = ["Visual", "Auditory", "Reading/Writing"]
print("\nSelect your learning style:")
for i, s in enumerate(styles):
    print(f"{i+1}. {s}")
style_choice = styles[int(input("Enter option number: ")) - 1]

# Combine student profile
student_profile = f"{subject_choice} {college_choice} {level_choice} {style_choice}"

# Combine mentor profiles
mentor_profiles = (
    mentors_df["expertise_subjects"] + " " +
    mentors_df["college"] + " " +
    mentors_df["mentoring_level"] + " " +
    mentors_df["mentoring_style"]
)

# Vectorize and compute similarity
vectorizer = CountVectorizer().fit_transform([student_profile] + mentor_profiles.tolist())
similarity_scores = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()

# Top 3 recommendations
top_indices = similarity_scores.argsort()[-3:][::-1]
top_mentors = mentors_df.iloc[top_indices]

# Output results
print(f"\nHi {name}, based on your inputs, here are the top 3 mentors for you:\n")
for i, row in top_mentors.iterrows():
    print(f"{row['name']} - Subject: {row['expertise_subjects']} | College: {row['college']} | Style: {row['mentoring_style']}")

print("\nThese are the Recommended Mentors for You  \nThank you for using the mentor recommendation system.")

# Ask for feedback
print("\nWe hope you found these recommendations helpful!")
rating = input("Please rate the recommendation system from 1 (Poor) to 5 (Excellent): ")

import csv
import os

# Ask for feedback
feedback_score = input("\nOn a scale of 1 to 5, how helpful were these mentor suggestions? ")

# Prepare user data dictionary
user_data = {
    "Name": name,
    "Preferred Subject": subject_choice,
    "Target College": college_choice,
    "Preparation Level": level_choice,
    "Learning Style": style_choice,
    "Recommended Mentors": ", ".join(top_mentors["name"].tolist()),
    "Feedback Score": feedback_score
}

# Save to CSV
log_file = "user_data_log.csv"
file_exists = os.path.isfile(log_file)

with open(log_file, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=user_data.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(user_data)

print("\n Your feedback has been saved. Thank you for helping us improve!")
