from fastapi import FastAPI
# from app.events.router import router as router_events
from app.Users.router import router as router_users
import uvicorn
app = FastAPI()
app.include_router(router_users)
