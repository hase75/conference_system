from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocalでセッションを定義している
# autocommit, sutoflushはコミットを自動でするかどうかの設定
# bindはengineとセッションを結びつけている

Base = declarative_base()
# declarative_baseという既にあるクラスを使ってDBの構造を名義する必要がある