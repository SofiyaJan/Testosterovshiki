from app.dao.base import BaseDAO
from app.Products.models import Product

class ProductDAO(BaseDAO):
  model = Product