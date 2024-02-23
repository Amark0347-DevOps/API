from motor.motor_asyncio import AsyncIOMotorClient
from ..model.models import Add_Course_Model, Add_Schedule, Add_Trainer, User_Login, User_SingUp
from fastapi.encoders import jsonable_encoder
from fastapi import status, HTTPException
class UserService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("FireArmTrainig")
        self.TrainerCollection = self.db.get_collection("Trainers")
        self.CourseCollection = self.db.get_collection("Courses")
        self.ScheduleCollection = self.db.get_collection("Schedule")
        self.Singup_LoginCollection = self.db.get_collection("Schedule")

    async def add_trainer(self, data):
        re = await self.TrainerCollection.insert_one(data)
        re1 = await self.TrainerCollection.find_one({"_id":re.inserted_id})
        return Add_Trainer(**re1)
    
    async def get_trainer(self):
        l =[]
        cursor = self.TrainerCollection.find()
        async for i in cursor:
            i["_id"]=str(i["_id"])
            l.append(i)
        return l
    
    async def add_course(self, data):
        re = await self.CourseCollection.insert_one(data)
        re1 = await self.CourseCollection.find_one({"_id":re.inserted_id})
        return Add_Course_Model(**re1)
    
    async def get_courses(self):
        l =[]
        cursor = self.CourseCollection.find()
        async for i in cursor:
            i["_id"]=str(i["_id"])
            l.append(i)
        return l
            
    
    async def add_schedule(self, data):
        re = await self.ScheduleCollection.insert_one(data)
        re1 = await self.ScheduleCollection.find_one({"_id":re.inserted_id})
        return Add_Schedule(**re1)
    
    async def get_schedule(self):
        l =[]
        cursor = self.ScheduleCollection.find()
        async for i in cursor:
            i["_id"]=str(i["_id"])
            l.append(i)
        return l
    

    async def signup_func(self, data)-> User_SingUp:
        if await self.Singup_LoginCollection.find_one({"phone":data.phone}):
            raise HTTPException(detail="User Already Register", status_code= status.HTTP_409_CONFLICT)
        else:
            re = await self.Singup_LoginCollection.insert_one(jsonable_encoder(data))
            if re:
                re1 = await self.Singup_LoginCollection.find_one({"_id":re.inserted_id})
                return User_SingUp(**re1)
            else:
                HTTPException(detail="data is not inserted", status_code=status.HTTP_400_BAD_REQUEST)
    

    async def login_func(self, data):
        re1 = await self.Singup_LoginCollection.find_one({"phone":data.phone})
        if re1:
            if re1["email"] == data.email:
                if re1["password"] == data.password:
                    return User_Login(**re1)
                else:
                    raise HTTPException(detail="Wrong Password", status_code=status.HTTP_400_BAD_REQUEST)
            else:
                raise HTTPException(detail="Wrong Email Address", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            raise HTTPException(detail="User not  Exist", status_code=status.HTTP_400_BAD_REQUEST)
