from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Diet(Base):
    __tablename__ = 'diets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date)
    total_calories = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)

    user = relationship("User", back_populates="diets")
    products = relationship("DietProduct", back_populates="diet")

class DietProduct(Base):
    __tablename__ = 'diet_products'
    id = Column(Integer, primary_key=True)
    diet_id = Column(Integer, ForeignKey('diets.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Float)

    diet = relationship("Diet", back_populates="products")
    product = relationship("Product", back_populates="diet_links")
