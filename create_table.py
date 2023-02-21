from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///project.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()


class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer(), primary_key=True)
    name = Column(String())


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer(), primary_key=True)
    name = Column(String())


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(245))
    description = Column(String(250))
    trailer = Column(String(250))
    year = Column(Integer())
    rating = Column(Integer())
    genre_id = Column(Integer(), ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer(), ForeignKey("director.id"))
    director = relationship("Director")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String())
    password = Column(String())
    name = Column(String())
    surname = Column(String())
    favorite_genre = Column(String(), ForeignKey("genre.name"))
    genre = relationship("Genre")
    

# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()