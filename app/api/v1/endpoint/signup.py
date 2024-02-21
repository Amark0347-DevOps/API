from ..routers import login_router, signup_router
from ....model.models import User_SingUp, User_Login
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from ....mongo.mongodb import connect_mongodb
from  ....services.user import UserService
@signup_router.post("/v1/signup")
async def singup(data:User_SingUp, db: AsyncIOMotorClient= Depends(connect_mongodb)):
    # re  = jsonable_encoder(data)
    userservice = UserService(db)
    re1 = await userservice.signup_func(data)
    return re1

@login_router.post("/v1/login")
async def login(data:User_Login, db:AsyncIOMotorClient = Depends(connect_mongodb)):
    # re  = jsonable_encoder(data)
    userservice = UserService(db)
    return await userservice.login_func(data)
