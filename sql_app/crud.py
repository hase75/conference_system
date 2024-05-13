from sqlalchemy.orm import Session
from . import models, schemas

# ユーザー一覧取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
    # db.query(models.User)でUserテーブルのDBを参照している
    # skipは最初から何番目を飛ばすかどうかの設定、limitは一度に何件取得するかの設定

# 会議室一覧取得
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

# 予約一覧取得
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

# ユーザー登録
def create_user(db: Session, user: schemas.User): # 3のFastAPI側で送信データを受け取る必要があるため、user: schemas.Userを引数に入れている
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # 4の受け取ったデータをDBに保存
    return db_user

# フォーム送信からDBに値を保存するまでの流れ
# 1.フォーム上でユーザー名を入力
# 2.送信ボタンを押すと、APIを叩く
# 3.FastAPI側で送信データを受け取る
# 4.受け取ったデータをDBに保存

# 会議室登録
def create_room(db: Session, room: schemas.Room):
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 予約登録
def create_booking(db: Session, booking: schemas.Booking):
    db_booking = models.Booking(
        user_id = booking.user_id,
        room_id = booking.room_id,
        booked_num = booking.booked_num,
        start_datetime = booking.start_datetime,
        end_datetime = booking.end_datetime
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking