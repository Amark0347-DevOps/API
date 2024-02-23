from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from app.mongo.mongodb import connect_mongodb, close_mongodb_connection
from app.api.v1.endpoint.add_schedule import add_course_schedule, get_course_schedule
from app.api.v1.endpoint.add_course import add_course_router, get_course_router
from app.api.v1.endpoint.add_trainer import add_trainer, get_trainer
from app.api.v1.endpoint.signup import signup_router, login_router
import logging.config
app = FastAPI()

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
})
# Configure CORS
origins = ["http://localhost:5000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_event_handler("startup", connect_mongodb)
app.add_event_handler("shutdown", close_mongodb_connection)
app.include_router(add_course_schedule)
app.include_router(add_trainer)
app.include_router(add_course_router)
app.include_router(get_course_router)
app.include_router(get_course_schedule)
app.include_router(get_trainer)
app.include_router(login_router)
app.include_router(signup_router)
if __name__ == "__main__":
    run("main:app", port=4522, host="localhost", reload=True)