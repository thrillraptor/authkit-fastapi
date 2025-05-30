# 🚀 FastAPI OAuth App

This repository provides a clean and minimal **FastAPI OAuth** project setup using Python's built-in `venv` for virtual environment management.

---

## 📚 Features

- FastAPI server setup
- Hot-reloading with Uvicorn
- Environment variable configuration
- Virtual environment via `venv`

---

## 🛠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔧 Setup

### 1. Clone the repository

```bash
https://github.com/thrillraptor/OAuth-FastAPI.git
cd OAuth-FastAPI
```

### 2. Create a virtual environment using `venv`

```bash
python -m venv venv
source venv/bin/activate
```

- #### On Windows
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`