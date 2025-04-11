  About the Project

This project is an AI/ML-based Personalized Mentor Recommendation System designed for law aspirants preparing for CLAT and similar entrance exams.
It helps match students with the most suitable mentors based on their learning preferences, academic goals, and preparation level. 
The objective is to enhance mentorship and guidance for aspirants by providing personalized recommendations, especially through the experience and expertise of previous CLAT toppers.

The system works by first collecting information from the student using multiple-choice questions (MCQs). 
Students provide their preferred subject (like Legal Reasoning, English, etc.), their target law college, current preparation level (Beginner to Advanced), and learning style (Visual, Auditory, or Reading/Writing). 
This input data is then used to generate a user profile which is compared with mentor profiles using a cosine similarity algorithm.

The mentor profiles are stored in a CSV file and include details like the mentor's name, area of expertise, associated college, mentoring level, and style. 
Based on the similarity score between the student's input and mentor profiles, the system recommends the top 3 best-matched mentors. 
Each recommendation includes the mentor’s name, subject expertise, college, and mentoring style. 
This ensures that students get mentorship from individuals who closely align with their learning needs.

Additionally, the system captures and stores student responses along with optional feedback scores in a CSV file. 
This data can later be used to improve the model with user insights and train more advanced recommendation algorithms.
Overall, this project is simple, functional, and scalable — with future potential to be developed into a full web or app-based solution for platforms like NLTI.