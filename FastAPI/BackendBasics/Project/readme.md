# TodoApp — FastAPI

This is a todo application I built while studying FastAPI. The goal was never to make something pretty — the focus is entirely on the backend: how the API is structured, how authentication works, how the database is managed, and how everything is tested.

The frontend exists just to make the app usable. It's server-side rendered with Jinja2 templates and Bootstrap via CDN. Don't judge the HTML.

---

## What the app does

Users can create an account, log in, and manage their own list of todos. Each todo has a title, description, priority from 1 to 5, and a completion status. There's also an admin role that can view and delete anyone's todos. Authentication is handled with JWT tokens stored in cookies, and the token expires after 20 minutes.

---

## Tech used

FastAPI, PostgreSQL, SQLAlchemy, Alembic for migrations, python-jose for JWT, passlib with bcrypt for passwords, Jinja2 for templates, and Pytest with SQLite in-memory for testing.

---

## How to run locally

Clone the repo, create a virtual environment and install the dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in your database credentials and secret key:

```env
DATABASE_URL=postgresql://your_user:your_password@localhost/your_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

Run the migrations and start the server:

```bash
alembic upgrade head
uvicorn Todoapp.main:app --reload
```

The app will be at `http://localhost:8000`.

---

## Running tests

The tests use SQLite in-memory so you don't need PostgreSQL running. Just run:

```bash
pytest
```

---

## Project structure

```
Todoapp/
├── alembic/            # migrations
├── routers/            # auth, todos, admin, users
├── test/               # all tests and fixtures
├── static/             # base.css and base.js (custom only)
├── templates/          # Jinja2 HTML templates
├── database.py
├── models.py
├── main.py
├── requirements.txt
└── .env.example
```

---

## What I learned

This project was where a lot of things clicked for me. I got comfortable with SQLAlchemy sessions, how dependency injection works in FastAPI with `Depends()`, how to structure routers, and how to test an API properly by overriding dependencies and using fixtures. Alembic was new to me and took a bit to understand, but it makes a lot of sense once you see it in action.

The authentication part was the most interesting — signing and decoding JWT tokens manually, handling expiration, and tying it all together with OAuth2PasswordBearer and cookies.

This is part of a larger learning path toward backend AI engineering. Next projects will go further into deployment, async patterns, and eventually ML serving.

