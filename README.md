# Simple Social

A simple social media backend/API built with **FastAPI** and **PostgreSQL**. It allows users to create accounts, log in, create posts, and like posts. The project uses **JWT authentication**, **dependency injection**, and **Alembic** for database migrations.

## Features

* User registration & login
* JWT-based authentication
* Create, update, delete posts
* Like/unlike posts
* PostgreSQL database
* Database migrations using Alembic
* Modular router structure (auth, posts, users, votes)


## Project Structure

```
app/
 ├── routers/
 │    ├── auth.py
 │    ├── post.py
 │    ├── user.py
 │    └── votes.py
 ├── config.py
 ├── database.py
 ├── main.py
 ├── models.py
 ├── oauth2.py
 ├── schemas.py
 └── utils.py
```

## Tech Stack

* **FastAPI** – Backend framework
* **PostgreSQL** – Database
* **SQLAlchemy** – ORM
* **Alembic** – Migrations
* **Pydantic** – Data validation
* **Python 3**

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/dipesh1dp/simple-social.git
cd simple-social
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables in `.env`

Example:

```
DATABASE_URL=postgresql://user:password@localhost:5432/socialdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run Alembic migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```


### Authentication
- `/user` → create user
- `/login` → get JWT token
- Protected routes require: Authorization: Bearer <token>

### Post/Vote
- `/posts` → create, get, update, delete posts
- `/vote` → like/unlike
