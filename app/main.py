from fastapi import FastAPI
# from app.events.router import router as router_events
from app.Users.router import router as router_users
from app.Products.router import router as router_product
from app.Diets.router import router as router_diet

import uvicorn
app = FastAPI()
app.include_router(router_users)
app.include_router(router_diet)
app.include_router(router_product)
