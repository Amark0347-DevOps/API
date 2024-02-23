from pydantic import BaseModel, ConfigDict, field_validator, Field, EmailStr
from fastapi import HTTPException, status 
class Add_Schedule(BaseModel):
    Selected_Course:str = Field(...)
    Day:str  = Field(...)
    Start_Time:str  = Field(...)
    End_Time:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Selected_Course":"Python",
                "Day":"Monday",
                "Start_Time":"12 PM",
                "End_Time":"3 PM",
            }
        }
    )


    # @field_validator("course_name")
    # def course_validate(cls, course_name):
    #     if len(course_name) >= 10:
    #         # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
    #         raise ValueError("Invalid Course Name")
    #     else:
    #         return course_name
        

class Add_Course_Model(BaseModel):
    Course:str =Field(...)
    Duration:str = Field(...)
    Sdate:str = Field(...)
    Edate:str = Field(...)
    Cost:str = Field(...)
    TrainerName:str = Field(...)
    Discount:str = Field(...)
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "Course":"Python",
                "Duration":"1 month",
                "Sdate":"5 jan",
                "Edate":"9 may",
                "Cost":"5000",
                "TrainerName":"amarjeet",
                "Discount":"10"
            }
         }
    )

    # @field_validator("enter_course")
    # def enter_course_validate(cls, enter_course):
    #     if len(enter_course)>=10:
    #         raise ValueError("crouse value error")
    #     else:
    #         return enter_course
        

class Add_Trainer(BaseModel):
    Trainer_Name:str = Field(...)
    Email:str  = Field(...)
    Phone:str  = Field(...)
    Experince:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Trainer_Name":"Amarjeet",
                "Email":"amark0347@gmail.com",
                "Phone":"9056678462",
                "Experince":"3 years"
            }
        }
    )

class User_Login(BaseModel):
    password:str= Field(...)
    email:str = Field(...)
    phone:str = Field(...)
    status_code:int = Field(default=status.HTTP_200_OK)
    message:str = Field(default="Successfully Registerd")
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "password":"Amarjeet",
                "email":"amarkila@gmail.com",
                "phone":"9056678462",
                "status_code":"200",
                "message":"Successfully Login"
            }
        }
    )

class User_SingUp(BaseModel):
    firstName:str =Field(...)
    lastName:str =Field(...)
    email:EmailStr =Field(...)
    phone: str =Field(...)
    password:str =Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "firstName": "bablu",
                "lastName": "Umrigar",
                "email": "bablueet@gmail.com",
                "countryCode": "+91",
                "phone": "1116789094",
                "password": "aaal@123",
                "dob": "28 Dec 2001",
                "gender": "Male",
                "bloodGroup": "+B",
                "status_code":"200",
                "message":"Successfully Registerd"

            }
        }
    )