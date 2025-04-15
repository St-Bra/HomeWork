from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

class Base(DeclarativeBase):
    pass

DATABASE_URL = "postgresql://postgres:09890@localhost:5432/eschool_db"

engine = create_engine(DATABASE_URL)

class Course(Base):
    __tablename__ = "Courses1"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_course1():
    session = Session()
