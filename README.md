# 🚀 Authentication for FastAPI
A minimal and developer-friendly FastAPI OAuth setup with Python's built-in venv for virtual environment management.

---

## 🔧 Setup

### 1. Clone the repository

```bash
https://github.com/thrillraptor/authkit-fastapi.git
cd authkit-fastapi
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
