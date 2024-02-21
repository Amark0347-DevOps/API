from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from fastapi import HTTPException, status
from ..core.config import settings
class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.mongo_uri, maxPoolSize=10, minPoolSize=5)
mongodb = MongoDB()

async def connect_mongodb():
    try:
        return mongodb.client
    except ServerSelectionTimeoutError as error:
        print(f"Database Server Con't Connect: {error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def close_mongodb_connection():
    return mongodb.client.close()

