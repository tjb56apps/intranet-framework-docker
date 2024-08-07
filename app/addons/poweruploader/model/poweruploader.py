from app.extensions.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Poweruploader(Base):
    __tablename__ = "poweruploader"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    department = Column(String)
    position = Column(String)
    table = Column(String)

    def __repr__(self):
        return f"<Post {self.username}>"

class Table(Base):
    __tablename__ = "table"

    id = Column(Integer, primary_key=True)
    table_name = Column(String)

    def __repr__(self):
        return f"<Post {self.table_name}>"

class Manual(Base):
    __tablename__ = "Manual"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(100))

    def __repr__(self):
        return f"<Manual {self.name}>"

class Hsemanhour062024(Base):
    __tablename__ = "Hsemanhour062024"

    id = Column(Integer, primary_key=True)
    no = Column(Integer)
    title = Column(String)
    date = Column(Date)
    company = Column(String)
    manpower = Column(Integer)
    manhour = Column(Integer)
    safemanhour = Column(Integer)
    itemtype = Column(String)
    path = Column(String)

    def __repr__(self):
        return f"<Hsemanhour062024 {self.title}>"