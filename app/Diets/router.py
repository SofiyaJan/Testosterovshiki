from fastapi import APIRouter, Depends
from app.Products.dao import ProductDAO
from app.Diets.dao import DietDAO, DietProductDAO
from app.Diets.shemes import Diet, DietProduct
from app.Products.shemes import Product
from app.Users.shemes import SUserAuth
from  app.Diets.models import Diet
from app.Users.dependencies import get_current_user
from  datetime import date
router = APIRouter(
  prefix="/Diet",
  tags=["DietInteraction"]
)

@router.post("/create")
async def create_diet(custom_date: date = date.today(),user: SUserAuth = Depends(get_current_user)):
    await DietDAO.add(user_id = user.id,
                      date = custom_date,
                      total_calories = 0,
                      proteins = 0,
                      fats = 0,
                      carbohydrates = 0)
    return "Рацион создан успешно"

@router.post("/find")
async def return_diet(custom_date: date = date.today(),user: SUserAuth = Depends(get_current_user)):
    diet = await DietDAO.find_one_or_none(date = custom_date,user_id = user.id) 
    return diet

@router.post("/add")
async def add_to_diet(id_diet: int,id_product: int,quntity: float,user: SUserAuth = Depends(get_current_user)):
    product = await ProductDAO.find_by_id(id_product)
    quntity_100 = quntity / 100
    await DietDAO.change_by_id(id =id_diet,total_calories = Diet.total_calories + product.calories * quntity_100,
                               proteins = Diet.proteins + product.proteins * quntity_100,
                               fats = Diet.fats + product.fats * quntity_100,
                               carbohydrates = Diet.carbohydrates + product.carbohydrates * quntity_100)
    await DietProductDAO.add(diet_id = id_diet,product_id = id_product,quantity = quntity)
    return "{product.name} успешно добавлена"
    

