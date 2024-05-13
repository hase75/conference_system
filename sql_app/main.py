from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # DBを作成

app = FastAPI()

def get_db(): #セッションを獲得するための関数
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# async def index():
#     return {"message": "Success"}

#Read
@app.get("/users", response_mode=List[schemas.User]) # Listは複数受けとる際に必要な設定
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): # Dependsは値を確立している(その値しか入ってこないようにしている)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# 処理の流れ（router→cruds→models→schemas）
# 1./usersにgetメソッドでアクセスがある
# 2.直下のread_usersという関数の処理が動く
# 3.引数のskip, limit, db（何も入ってこなければデフォルト値）がget_usersという関数に入る
# 4.crud処理で指定された型のデータをList形式で全て受け取る
# 5.usersにはList形式のユーザー一覧が入っていて、それをreturnしている
# 6.response_modeにはschemasで指定された形のデータしか受け取らないため、returnで返されたList形式のUserデータを受け取ることができた

@app.get("/rooms", response_mode=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/bookings", response_mode=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

#Create
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/rooms", response_model=schemas.Room)
async def create_room(room: schemas.Room, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)

@app.post("/bookings", response_model=schemas.Booking)
async def create_booking(booking: schemas.Booking, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)