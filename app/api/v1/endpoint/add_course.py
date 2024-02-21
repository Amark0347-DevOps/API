from ..routers import add_course_router, get_course_router
from ....model.models import Add_Course_Model
from fastapi import Depends
from ....mongo.mongodb import connect_mongodb
from ....services.user import UserService
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
@add_course_router.post("/v1/add-course")
async def select_course_func(data:Add_Course_Model, db:AsyncIOMotorClient = Depends(connect_mongodb)):
    re  = jsonable_encoder(data)
    userservice = UserService(db)
    re = await userservice.add_course(re)
    return re 

@get_course_router.get("/v1/get-courses")
async def get_all_courses(db:AsyncIOMotorClient = Depends(connect_mongodb)):
    userservice = UserService(db)
    return await userservice.get_courses()
