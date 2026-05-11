# Todo API

A simple and clean REST API for managing your todos, built with FastAPI and SQLite. This was built as part of a learning project to understand how FastAPI handles database connections, dependency injection, and request validation.

## What it does

You can create, read, and update todos. Each todo has a title, a description, a priority level, and a completion status. The API validates everything before touching the database, so you won't end up with garbage data.

## Tech stack

- **FastAPI** — the web framework
- **SQLAlchemy** — ORM for database interaction
- **SQLite** — lightweight local database (stored as `todos.db`)
- **Pydantic** — request body validation

## Getting started

### Requirements

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
pip install fastapi sqlalchemy uvicorn
```

### Running the server

```bash
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`. The database file `todos.db` is created automatically on first run — no setup needed.

Once the server is running, you can explore the interactive docs at `http://127.0.0.1:8000/docs`.

## Project structure

```
__init__.py
main.py        # Routes and app entry point
models.py      # SQLAlchemy table definition
database.py    # Database engine and session setup
todos.db       # SQLite database (auto-generated)
```

## API reference

### Get all todos

```
GET /
```

Returns a list of all todos in the database.

**Response `200 OK`**
```json
[
  {
    "id": 1,
    "title": "Study FastAPI",
    "description": "Finish section 8 of the course",
    "priority": 3,
    "complete": false
  }
]
```

---

### Get a single todo

```
GET /todo/{todo_id}
```

Returns a single todo by its ID.

| Parameter | Type | Rules |
|-----------|------|-------|
| `todo_id` | int | must be greater than 0 |

**Response `200 OK`** — returns the todo object

**Response `404 Not Found`**
```json
{ "detail": "Todo not found." }
```

---

### Create a todo

```
POST /todo
```

Creates a new todo. The request body is validated before anything hits the database.

**Request body**
```json
{
  "title": "Study FastAPI",
  "description": "Finish section 8 of the course",
  "priority": 3,
  "complete": false
}
```

| Field | Type | Rules |
|-------|------|-------|
| `title` | string | min 3 characters |
| `description` | string | min 3, max 100 characters |
| `priority` | int | between 1 and 5 (inclusive) |
| `complete` | bool | true or false |

**Response `201 Created`** — no body returned

**Response `422 Unprocessable Entity`** — if any field fails validation

---

### Update a todo

```
PUT /todo/{todo_id}
```

Updates an existing todo. Requires the full object in the request body — all fields are replaced.

| Parameter | Type | Rules |
|-----------|------|-------|
| `todo_id` | int | must be greater than 0 |

**Request body** — same structure as POST

**Response `204 No Content`** — no body returned

**Response `404 Not Found`**
```json
{ "detail": "Todo not found" }
```

---

## How database sessions work

Each request gets its own database session, which is automatically closed when the request finishes — even if something goes wrong. This is handled by the `get_db` dependency:

```python
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
```

FastAPI injects this session into every route that needs it via `Depends(get_db)`, so you never have to manage connections manually.

## Notes

- This project uses SQLite, which is great for local development and learning. For production, you'd swap the database URL in `database.py` for PostgreSQL or MySQL — everything else stays the same.

