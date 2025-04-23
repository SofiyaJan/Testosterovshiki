from sqlalchemy import Column, Integer, ForeignKey, Date, Computed, String, Float
from app.database import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    height = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    obesity_level = Column(String, nullable=True)

    #goals = relationship("Goal", back_populates="user")
    #diets = relationship("Diet", back_populates="user")
    #analyses = relationship("Analysis", back_populates="user")
    #motivations = relationship("Motivation", back_populates="user")

class Motivation(Base):
    __tablename__ = 'motivations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    level = Column(String)
    message_type = Column(String)
    message_text = Column(Text)
    created_at = Column(Date)

    #user = relationship("User", back_populates="motivations")
