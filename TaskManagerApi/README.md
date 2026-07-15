# Task Manager API with JWT Authentication

A RESTful Task Manager API built using **FastAPI**, **SQLite**, **SQLAlchemy ORM**, **Pydantic**, and **JWT Authentication**. The API allows users to register, log in, and securely manage their own tasks through protected REST endpoints.

---

## Features

### Authentication

- User Registration (Signup)
- User Login
- JWT Authentication
- Password Hashing using Passlib (bcrypt)
- Protected Routes
- Get Current Logged-in User (`/auth/me`)

### Task Management

Authenticated users can:

- Create Tasks
- View All Tasks
- View a Single Task
- Update Tasks
- Delete Tasks

Each task belongs to the authenticated user, ensuring users can only access and manage their own tasks.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| FastAPI | REST API Framework |
| SQLite | Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| python-jose | JWT Authentication |
| Passlib (bcrypt) | Password Hashing |
| Uvicorn | ASGI Server |

---

## Project Structure

```

> **Note:** `tasks.db` is generated automatically when the application runs and is excluded from Git.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/<your-github-username>/TaskManagerApi.git
cd TaskManagerApi
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/signup` | Register a new user |
| POST | `/auth/login` | Authenticate user and generate JWT token |
| GET | `/auth/me` | Get the currently logged-in user |

---

## Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a specific task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## Security

- Passwords are securely hashed using Passlib (bcrypt).
- JWT Authentication protects all task endpoints.
- Users can only access and manage their own tasks.
- Proper HTTP status codes are returned for unauthorized or invalid requests.

---

## Dependencies

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib
- bcrypt
- python-jose
- python-multipart
- Uvicorn

---

## HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

## Assignment Features Implemented

### Authentication

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Protected Routes
- Current User Endpoint

### Task Management

- Create Task
- View All Tasks
- View Single Task
- Update Task
- Delete Task

### Database

- SQLite Database
- SQLAlchemy ORM
- User–Task Relationship

---

## Future Enhancements

- Refresh Token Support
- Forgot Password
- Email Verification
- Search & Filter Tasks
- Pagination
- Docker Support
- Role-Based Access Control (RBAC)

---

## Author

**Developed by:** Gayathri

Backend Developer Evaluation Assignment built using **FastAPI**, **SQLite**, **SQLAlchemy ORM**, **JWT Authentication**, and **REST APIs**.