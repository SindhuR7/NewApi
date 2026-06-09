from fastapi import FastAPI
from .config.database import engine,Base
from .routers.student_routes import studentRouter

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(studentRouter)

@app.get("/")
def reply():
    return {"message" : "Server is running"}