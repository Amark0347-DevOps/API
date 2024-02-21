from ..routers import add_trainer, get_trainer
from ....model.models import Add_Trainer
from fastapi import Depends
from ....mongo.mongodb import connect_mongodb
from ....services.user import UserService
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
@add_trainer.post("/v1/add-trainer")
async def add_employe(data:Add_Trainer, db:AsyncIOMotorClient = Depends(connect_mongodb)):
    re  = jsonable_encoder(data)
    userservice = UserService(db)
    re = await userservice.add_trainer(re)
    return re 

@get_trainer.get("/v1/get-trainers")
async def get_all_courses(db:AsyncIOMotorClient = Depends(connect_mongodb)):
    userservice = UserService(db)
    return await userservice.get_trainer()
