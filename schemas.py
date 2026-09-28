from pydantic import BaseModel, Field, ConfigDict

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    department: str = Field(min_length=2, max_length=50)

class EmployeeUpdate(BaseModel):
      name: str = Field(min_length=2, max_length=50)
      department: str = Field(min_length=2, max_length=50)
      
class EmployeeResponse(BaseModel):
        id: int
        name: str
        department: str

        model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
      username: str = Field(min_length=3, max_length=50)
      email: str
      password: str = Field(min_length=6, max_length=100)

class UserResponse(BaseModel):
      id: int
      username: str
      email: str

      model_config = ConfigDict(from_attributes=True)

