from app.dao.base import BaseDAO
from app.Diets.models import DietProduct, Diet

class DietDAO(BaseDAO):
  model = Diet

class DietProductDAO(BaseDAO):
  model = DietProduct