from pydantic import BaseModel
from datetime import datetime
class Diet(BaseModel):
    user_id: int
    date: datetime
    total_calories: float
    proteins: float
    fats: float
    carbohydrates: float
    #user = relationship("User", secondary="diet_products", back_populates="diets")

class DietProduct(BaseModel):
    diet_id : int
    product_id: int