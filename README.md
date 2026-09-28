# Employee Management API

A RESTful Employee Management API built using Python and FastAPI.

This project provides employee CRUD operations, user registration and login, JWT-based authentication, and database integration using SQLALchemy and SQLite.


## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (JSON Web Token)
- Passlib / bcrypt
- Uvicorn


## Features

- User registration
- User login
- Password hashing using bcrypt
- JWT-based authentication
- Protected employee API endpoints
- Create new employees
- View all employees
- View an employee by ID
- Update employee details
- Delete employees
- Filter employees by department
- Duplicate email and username validation
- Error handling for invalid or missing employees


## API Endpoints

### Users

- POST /users/register - Register a new user
- POST /users/login - Login and receive a JWT access token

### Employees

- GET /employees - Get all employees
- GET /employees/{employee_id}- Get employee by ID
- GET /employees/filter/ - Filter employees by department
- POST /employees - Create a new employee
- PUT /employees/{employee_id} - Update an employee
- DELETE /employees/{employee-id} - Delete an employee


## How to Run the Project

1. clone the repository

2. Install the required dependencies

pip install -r requirements.txt

3. Create a '.env' file and add a secret key

4. Start the FastAPI server

5. Open Swagger UI in the browser at '/docs'