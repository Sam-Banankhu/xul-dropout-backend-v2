from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from app.routes import auth, teacher, students, classes, users, ml_model
from app.middleware import add_cors_middleware


app = FastAPI(title="School Management System", description="A system for managing a school", version="1.0.0")
add_cors_middleware(app)



@app.get("/", include_in_schema=False)
async def root():
    """
    Root endpoint that redirects to the API documentation
    """
    return RedirectResponse(url="/docs")

app.include_router(ml_model.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(teacher.router)
app.include_router(students.router)
app.include_router(classes.router)


