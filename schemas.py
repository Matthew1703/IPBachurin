from pydantic import BaseModel

class Application(BaseModel):
    name: str
    numberOfPeople: int
    whereFrom: str
    whereTo: str
    data: str
    time: str
    phoneNumber: str
    money: int
