from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DbConfig:
    def __init__(self):
        self.__engine = create_engine('sqlite:///../DB/simple.db')
        Base.metadata.create_all(self.__engine)
        self.__session = None

    def get_engine(self):
        return self.__engine

    def create_session(self):
        Base.metadata.bind = self.__engine
        temp = sessionmaker(bind=self.__engine)
        self.__session = temp()

    def get_session(self):
        return self.__session
