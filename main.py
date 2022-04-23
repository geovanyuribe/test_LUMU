from fastapi import FastAPI
from routers import router
import uvicorn
import os

app = FastAPI(
    title="Test_LUMU",
    description="Deploy of the fraud prediction model for LUMU's test",
    version="0.1")

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, port=os.environ.get('PORT', 8080), host='0.0.0.0')