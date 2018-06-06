from sqlalchemy import Column, Integer, String
from src.models.base import Base


class Homeworks(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, nullable=False)  # foreign_key
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    file_path = Column(String(50), nullable=False)
    deadline = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    modified = Column(String(30), nullable=True)
