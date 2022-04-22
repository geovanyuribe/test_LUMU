from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="Test_LUMU",
    description="Deploy of the fraud prediction model for LUMU's test",
    version="0.1")

app.include_router(router)