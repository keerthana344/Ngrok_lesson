from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.User_routes import router as user_router
from sqlalchemy import create_engine
from db import get_db,DATABASE_URL
import os
from models import Base
app = FastAPI()

#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

# to create database

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

@app.get("/")
def read_root():  
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)