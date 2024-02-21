from ..routers import add_course_schedule , get_course_schedule
from ....model.models import Add_Schedule
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from ....mongo.mongodb import connect_mongodb
from  ....services.user import UserService
@add_course_schedule.post("/v1/add-schedule")
async def select_course_func(data:Add_Schedule, db: AsyncIOMotorClient= Depends(connect_mongodb)):
    re  = jsonable_encoder(data)
    userservice = UserService(db)
    re1 = await userservice.add_schedule(re)
    return re1

@get_course_schedule.get("/v1/get-schedules")
async def get_all_courses(db:AsyncIOMotorClient = Depends(connect_mongodb)):
    userservice = UserService(db)
    return await userservice.get_schedule()
