from sqlalchemy import Column,Integer,String
from app.core.database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, Primary_key = True, Index=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
