from fastapi import FastAPI
import models
from db import engine
from routes import question_routes, choice_routes

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(question_routes.router, prefix="/questions", tags=["Questions"])
app.include_router(choice_routes.router, prefix="/choices", tags=["Choices"])
