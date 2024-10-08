# Expense Tracker App

A web application built using Django to help users efficiently manage and categorize their expenses. It provides a user-friendly interface, secure authentication, and interactive data visualization for expense analysis.

## Features

- **User Authentication and Authorization**: Integrated with Django's inbuilt authentication and authorization system for secure user login, registration, and account management.
- **Responsive Design**: Developed with `Tailwind CSS` to ensure the application is fully responsive and looks great on any device.
- **Expense Tracking**: Allows users to add, edit, delete, and categorize their expenses with ease.
- **Interactive Graphs**: Uses `Chart.js` to display interactive graphs that give a detailed analysis of expenses over time.
- **Efficient Data Management**: Provides robust backend functionalities for managing expense records and categories.

## Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, Tailwind CSS
- **Charts and Visuals**: Chart.js
- **Authentication**: django-allauth

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/expense-tracker-app.git
   cd expense-tracker-app
   ```

2. **Install Dependencies**

   Make sure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to access the app.

## Usage

1. **Register**: Create an account to start managing your expenses.
2. **Add Expenses**: Enter details like amount, date, and category for each expense.
3. **Analyze**: View your expenses in the form of detailed, interactive charts.
4. **CRUD Operations**: Edit or delete your expenses as needed.

## Contributing

Feel free to submit issues or fork the repository and make a pull request. Contributions are always welcome!

## Contact

If you have any questions or feedback, feel free to contact me via [harshs0891@gmail.com.](mailto:harshs0891@gmail.com)
