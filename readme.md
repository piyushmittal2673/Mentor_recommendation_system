# Mentor Recommendation System – NLTI ( Internship Submission )

## Objective
To build an ML-based recommendation system that suggests the top 3 suitable mentors (CLAT toppers) to law aspirants based on their profile.

## Features
- Input: User name and multiple-choice answers on:
  - Preferred subject
  - Target college
  - Current preparation level
  - Learning style
- Output: Top 3 matched mentors based on content-based filtering and cosine similarity.

## Approach
- Used CountVectorizer to vectorize textual inputs.
- Applied cosine similarity to compare student profile with mentor profiles.
- Recommended the top 3 mentors based on highest similarity.

## Technologies Used
- Python and its libraries
- scikit-learn
- pandas

## How to Run
1. Ensure Python and `scikit-learn` are installed:
   
   pip install pandas scikit-learn

2. Run the script in terminal or VS Code:
   
   python recommend_mentors.py
   

## Dataset
Mock mentor data is stored in `mentors.csv` with fields:
- Name
- Expertise Subject
- College
- Mentoring Level
- Mentoring Style

## Improvements Over Time
- Add user feedback and continuously update model.
- Use real mentor-student interaction data for fine-tuning.
- Extend to a web-based dashboard or Streamlit app.

## Feedback Logging
(Planned Feature): User inputs and feedback will be saved for future model improvements.
