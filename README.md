# Project
Personal Finance Tracker 
Video Demo: https://youtu.be/H02IPHkGb5Q
Description: 

Personal Finance Tracker
Hello and welcome to the Personal Finance Tracker, a web application designed to help users manage their finances by tracking income and expenses, categorizing transactions, setting monthly budgets, and visualizing spending patterns using a web version built with Python (using Streamlit). Working with pandas for data handling and matplotlib for visualizations, this project allows users to track their finances in real-time through an interactive interface. It’s great for personal finance, offering automatic and manual categorization of transactions, monitoring of account balances, budget alerting, and pie chart graphics. This README provides a thorough rundown of the project, its files, what they do, and the thought processes behind it.

Project Overview
The Personal Finance Tracker allows users to record either income or expenses with categorical allocation including Food, Transport, Bills, Health, Shopping, Entertainment, Education, Travel, and Miscellaneous while monitoring their total balance and budget. The user interacts with a Streamlit web app where they can enter transactions, set a monthly budget for each category, view a per-category breakdown of a summary, and an insightful pie chart of where they spend their money. The app does a good job of balancing automation — defining account categories based on a keyword search — and user flexibility (with the added ability to manually select which category to assign) for a quick, efficient and accurate way to manage your finances. This level of balance keeps the app usable by novices while still providing advanced tools for power users, making the app suitable for many financial management interests.

Files and Their Functionality
The project includes three key files:
•	project.py: This file contains the core Python code, including the main() function for the Streamlit web app and three custom functions: categorize_expense(), calculate_balance(), and generate_summary(). The main() function handles user interaction, enabling transaction input, budget setting, and the display of summaries and visualizations in a clean, web-based format. categorize_expense() categorizes transactions automatically via keywords or manually via user input, calculate_balance() computes the total balance, and generate_summary() provides a breakdown of transactions by category. A global categories dictionary defines the categorization rules, ensuring consistency across the app.
•	test_project.py: This file includes pytest tests for the three custom functions in project.py. It features test_categorize_expense(), test_calculate_balance(), and test_generate_summary(), verifying function behavior for various transaction scenarios, such as different amounts, descriptions, and edge cases (e.g., empty lists or mismatched keywords). These tests ensure the app’s core logic is reliable and bug-free, following best practices for software testing.
•	requirements.txt: This file lists the required libraries—streamlit, pandas, matplotlib, and pytest—enabling users to install dependencies with pip install -r requirements.txt for a reproducible setup. This ensures anyone can run the project on their system without compatibility issues.

Functionality and Features
Key features include:
•	Transaction Logging: Users can input income or expense amounts, descriptions, and categories, choosing between manual selection or automatic keyword-based categorization for ease and accuracy.
•	Categorization: Transactions are organized into eight predefined categories (plus Miscellaneous) using keyword matching or user choice, ensuring precise tracking and analysis of spending patterns.
•	Balance and Budget Tracking: The app calculates the total balance and compares it to a user-defined monthly budget, providing alerts if the user exceeds their budget, helping maintain financial discipline.
•	Data Visualization: A pie chart displays spending by category, focusing on expenses to offer clear, visual insights into financial habits, making it easy to identify areas for savings.
•	Interactive Interface: Streamlit provides a web-based, user-friendly experience accessible in any browser, with real-time updates and a clean layout that enhances usability for all users.

Design Choices and Rationale
We made several key decisions to keep the project simple and effective:
•	Streamlit for Web Interface: We chose Streamlit because it was required for this project and offers a simple, clean, and top-notch user experience. Its web-based nature makes the app accessible and visually appealing, perfect for real-time financial tracking.
•	Both Automatic and Manual Categorization: We included automatic categorization with keywords for speed and convenience, but added manual selection so users can correct or specify categories, ensuring accuracy for unique or unclear transactions.
•	Global Categories List: We placed the categories dictionary globally to avoid confusion and make it easy to use across the app, keeping the code straightforward and consistent.
•	Expense-Only Visualization: We decided to show only expenses in the pie chart to keep it focused on spending, making it easier for users to understand their habits and prioritize savings.
•	Focus Tests on Core Functions: We tested only the main functions (not the UI) because they’re the core logic, and testing them is simpler, faster, and covers the most critical parts of the app.
This project required significant effort, surpassing typical problem set complexity with its integration of web development, data processing, and visualization. I’m proud of creating a practical, user-friendly tool for financial management. Future enhancements could include saving data to files or adding more detailed analytics, but the current version provides a solid, effective foundation for personal finance tracking.
