from fastapi import FastAPI
from app.db.session import engine, Base

from app.api.routes import user, auth

app = FastAPI(title="OAuth API")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)