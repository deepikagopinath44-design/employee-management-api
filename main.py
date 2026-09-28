from fastapi import FastAPI
from routes.employees import router as employee_router
from routes.users import router as user_router

from models import create_tables

app = FastAPI()

create_tables()

app.include_router(employee_router)
app.include_router(user_router)
