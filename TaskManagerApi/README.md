# Simple FastAPI Task Manager API

## Project Overview

This project is a simple Task Manager REST API built using **FastAPI**, **SQLite**, **SQLAlchemy ORM**, and **Pydantic**. It allows users to create, view, update, and delete tasks while demonstrating REST API development, database integration, request validation, and CRUD operations.

---

## Objective

Develop a backend application that manages tasks using REST APIs with the following features:

* Create a new task
* View all tasks
* Update an existing task
* Delete a task

---

## Technologies Used

* Python 3.x
* FastAPI
* SQLite
* SQLAlchemy ORM
* Pydantic
* Uvicorn

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/TaskManagerAPI.git
```

### 2. Open the project

```bash
cd TaskManagerAPI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

---

## Swagger Documentation

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| POST   | `/tasks`           | Create a new task  |
| GET    | `/tasks`           | Retrieve all tasks |
| PUT    | `/tasks/{task_id}` | Update a task      |
| DELETE | `/tasks/{task_id}` | Delete a task      |

---

## Sample Request

```json
{
  "title": "Complete FastAPI Assignment",
  "description": "Build CRUD APIs using FastAPI",
  "status": "Pending"
}
```

---

## Sample Response

```json
{
  "id": 1,
  "title": "Complete FastAPI Assignment",
  "description": "Build CRUD APIs using FastAPI",
  "status": "Pending"
}
```

---

## Features

* RESTful API development
* CRUD operations
* SQLite database integration
* SQLAlchemy ORM
* Pydantic validation
* Automatic Swagger documentation
* Proper HTTP status codes
* Clean project structure
* Error handling

---

## Future Improvements

* Search tasks
* Filter by status
* Pagination
* Authentication
* Docker support

---

## Author

Developed as part of the **FastAPI Task Manager API Evaluation Assignment**.
