PROGRESSO
Basic Details
Team Name: Quite tides
Team Members
Member 1: LENA ANTONY - MUTHOOT INSTITUTE OF TECHNOLOGY AND SCIENCE,KOCHI
Member 2: ANAMIKA RAVI - MUTHOOT INSTITUTE OF TECHNOLOGY AND SCIENCE,KOCHI
Hosted Project Link
(https://progresso-2.onrender.com/)

Project Description
PROGRESSO is a web-based student productivity platform that helps students manage their academic tasks, expenses, and extracurricular activities in one place. It allows users to track attendance, assignments, participation, and personal spending through an organized dashboard. The platform is built using Python (Flask), HTML, CSS, and SQLite for efficient data management. Its goal is to improve student organization, productivity, and overall personal growth through a centralized system.
The Problem statement
College students often face difficulty managing their academic responsibilities, extracurricular activities, and personal expenses due to the lack of a centralized system. Existing college portals mainly focus on attendance and marks, while other important aspects like assignment tracking, activity participation, collaboration, and expense management are handled separately or manually. This leads to poor organization, missed deadlines, and inefficient productivity. Therefore, there is a need for an integrated platform that helps students efficiently manage and monitor their academic and personal development in one place.


The Solution
PROGRESSO provides a centralized web-based platform that enables students to manage their academic tasks, track attendance and assignments, record extracurricular activities, and monitor personal expenses in one system. It offers an organized dashboard where students can easily view their progress and stay updated with their responsibilities. By integrating multiple productivity tools into a single platform, PROGRESSO improves student organization, efficiency, and overall personal development.

Technical Details
Technologies/Components Used
For Software:

Languages used: [e.g., JavaScript, Python, Java]
Frameworks used: [e.g., React, Django, Spring Boot]
Libraries used: [e.g., axios, pandas, JUnit]
Tools used: [e.g., VS Code, Git, Docker]
For Hardware:

Not applicable, as this is a software-based project
Features
List the key features of your project:

Feature 1:  Expense Manager
Helps students track daily expenses and monitor their financial spending.
Feature 2:  Activity Tracker
  This shows the activity participation page where students can record extracurricular activities.

Feature 3:  Assignment Planner with Due Date Reminder
Enables students to add assignments with subjects and due dates, helping them stay organized and avoid missing deadlines.
Feature 4:  Dashboard Overview
 Provides a centralized dashboard showing academic progress, upcoming assignments, activities, and expenses.

Implementation
For Software:
Installation
Installation commands - pip install flask gunicorn,
Run
Run commands - python app.py
Open browser
For Hardware:
Not applicable, as this is a software-based project

Circuit Setup
[Explain how to set up the circuit]

Project Documentation
For Software:
<img width="1770" height="871" alt="Screenshot 2026-02-21 091220" src="https://github.com/user-attachments/assets/95a73ad0-69ba-4dd5-9d93-1107945720ba" />
login page
User name:alex
Password:12345
<img width="1916" height="909" alt="Screenshot 2026-02-21 093539" src="https://github.com/user-attachments/assets/eda2121d-383a-4e13-b602-5ba12df6c683" />
dashboard
<img width="1919" height="908" alt="Screenshot 2026-02-21 093554" src="https://github.com/user-attachments/assets/2dab673f-9eb8-4446-a863-ffbbca8e7d93" />
activity point 
<img width="1913" height="896" alt="Screenshot 2026-02-21 093612" src="https://github.com/user-attachments/assets/fa560ce1-4574-4565-a39c-05ec1ee4b376" />
assignment planner
<img width="1917" height="909" alt="Screenshot 2026-02-21 093627" src="https://github.com/user-attachments/assets/753e5b9c-4b54-4e1f-bc3a-cab523567500" />
expense



Diagrams
System Architecture:

Architecture Diagram Explain your system architecture - components, data flow, tech stack interaction
The PROGRESSO system follows a three-tier web architecture consisting of the Presentation Layer, Application Layer, and Data Layer.
Components:
1. Presentation Layer (Frontend)
Built using HTML, CSS, and JavaScript


Provides user interface such as Dashboard, Assignment Planner, Expense Tracker, and Activity Tracker


Handles user input and displays results


2. Application Layer (Backend)
Built using Python Flask framework


Processes user requests


Handles business logic such as assignment reminders, attendance tracking, and expense calculations


Communicates between frontend and database

Application Workflow:
User interacts with web interface


Request is sent to Flask backend


Backend processes request


Data is stored or retrieved from SQLite database


Backend sends response to frontend


Frontend displays updated information to user


Workflow Add caption explaining your workflow
User (Browser)
       │
       ▼
Frontend (HTML, CSS, JavaScript)
       │
       ▼
Backend (Flask - Python)
       │
       ▼
Database (SQLite)
       │
       ▼
Response back to User
Additional Documentation
For Web Projects with Backend:
API Documentation
Base URL: https://progresso.onrender.com

Endpoints
Assignment Planner
GET /assignments
Description:
 Retrieves all assignments with due dates and status (Upcoming / Overdue).
Parameters:
param1 (string): [Description]
param2 (integer): [Description]
{
  "status": "success",
  "data": [
    {
      "title": "Physics Record",
      "due_date": "2026-02-25",
      "status": "Upcoming"
    }
  ]
}

POST /add_assignment
Description:
 Adds a new assignment with due date for reminder tracking.
Request Body:
{
 "title": "Math Assignment",
 "due_date": "2026-03-01"
}
GET /expenses
Description:
 Retrieves budget and spending details.
Response:
{
 "status": "success",
 "data": {
   "budget": 5000,
   "total_spent": 3200,
   "remaining_balance": 1800
 }
}
POST /add_expense
Description:
 Adds a new expense entry.
Request Body:
{
 "amount": 250,
 "category": "Food",
 "date": "2026-02-21"
}
POST /set_budget
Description:
 Sets or updates the monthly budget.
Request Body:
{
 "budget": 5000
}
GET /activities
Description:
Retrieves activity participation records and total points earned.
Response:
{
 "status": "success",
 "data": {
   "total_points": 40,
   "activities": [
     {
       "activity_name": "Tech Fest",
       "points": 10,
       "date": "2026-02-15"
     }
   ]
 }
}

POST /add_activity
Description:
Adds a new activity participation with earned points.
Request Body:
{
 "activity_name": "Coding Competition",
 "points": 15,
 "date": "2026-02-20"
}
Response:
{
 "status": "success",
 "message": "Activity added successfully"
}




