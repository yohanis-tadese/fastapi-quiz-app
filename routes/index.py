from routes import question_routes, choice_routes

def setup_routes(app):
    app.include_router(question_routes.router, prefix="/questions", tags=["Questions"])
    app.include_router(choice_routes.router, prefix="/choices", tags=["Choices"])


# re-export for easier imports elsewhere
__all__ = ["setup_routes"]
