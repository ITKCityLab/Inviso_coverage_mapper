from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Transmissions(Base):
    __tablename__ = 'transmission_record'

    id = Column(Integer, primary_key=True, index=True)
    #data = Column('data', JSON, nullable=False)
    transmission = Column('transmission', String, nullable=False)
    inserted = Column('inserted',DateTime(timezone=True), default=func.now())