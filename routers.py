import random
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from models import Application

router = APIRouter()


@router.post("/new_application")
def add_application(dct: dict, db: Session = Depends(get_db)):
    dct["employee"] = random.randint(1,5)
    application = Application(**dct)
    db.add(application)
    db.commit()
    return {"status": 200}

@router.get("/applications")
def print_applications(db: Session = Depends(get_db)):
    applications = db.query(Application).all()
    return applications

@router.delete("/applications")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    db.query(Application).filter(Application.id==application_id).delete()
    db.commit()
    return {"status": 200}

@router.put("/applications")
def update_application(data: dict, db: Session = Depends(get_db)):
    db.query(Application).where(Application.id==data["id"]).update(
        {Application.whereFrom:data["whereFrom"],Application.employee:data["employee"],
         Application.whereTo:data["whereTo"],Application.numberOfPeople:data["numberOfPeople"],
         Application.phoneNumber:data["phoneNumber"], Application.money:data["money"],
         Application.time:data["time"]})
    db.commit()
    return {"status": 200}

