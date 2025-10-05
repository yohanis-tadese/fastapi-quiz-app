from fastapi import FastAPI
from config.db import engine
from models import index as model_index
from routes import index as routes_index

app = FastAPI()
model_index.Base.metadata.create_all(bind=engine)

routes_index.setup_routes(app)
