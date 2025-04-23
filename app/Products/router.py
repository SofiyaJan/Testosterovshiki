from fastapi import APIRouter, Depends
from app.Products.dao import ProductDAO
from app.Diets.dao import DietDAO, DietProductDAO
from app.Diets.shemes import Diet, DietProduct
from app.Products.shemes import Product
from app.Users.shemes import SUserAuth
from app.Users.dependencies import get_current_user
router = APIRouter(
  prefix="/Product",
  tags=["ProductInteraction"]
)

@router.post("/add")
async def adding_product(product: Product):
    await ProductDAO.add(name = product.name,
                         calories = product.calories,
                         proteins = product.proteins,
                         fats = product.fats,
                         carbohydrates = product.carbohydrates
                         )
    return "Продукт добавлен в базу"
    
@router.post("/search")
async def find_product(product_name: str):
    product_list = await  ProductDAO.find_all(name = product_name)
    return product_list

    