# Flask CRUD Operations App

This is a simple Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using an SQLite database.

## Getting Started

### Prerequisites

Before running this application, ensure you have the following:

- Python (3.6 or higher)
- Flask (installed via `pip install flask`)
- Flask SQLAlchemy (installed via `pip install flask_sqlalchemy`)
- Requests library (for generating random data, installed via `pip install requests)

### Installation and Usage

Follow these steps to run the application:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the app in your web browser at `http://127.0.0.1:5000`.

## Endpoints

- **POST /create:** Create a new entry in the database.
- **GET /read:** Retrieve all entries from the database.
- **GET /read/{id}:** Retrieve an entry by ID from the database.
- **PUT /update/{id}:** Update an entry by ID in the database.
- **DELETE /delete/{id}:** Delete an entry by ID from the database.

## Important Notes

- This application is for educational purposes and demonstrates basic CRUD operations using Flask and an SQLite database. In a production environment, you might want to use more advanced database systems and implement additional security measures.
- Please review the code and documentation for a better understanding of how the application works.

---
