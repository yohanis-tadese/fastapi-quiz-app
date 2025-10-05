from fastapi import FastAPI
from config.db import engine
from models import index as model_index
from routes import index as routes_index
from error_handlers import (
    validation_exception_handler,
    http_exception_handler,
    generic_exception_handler
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
model_index.Base.metadata.create_all(bind=engine)

routes_index.setup_routes(app)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
