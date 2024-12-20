from fastapi import FastAPI
import uvicorn
from routes import base, data
from helpers.config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(title="Mini RAG")

@app.on_event("startup")
async def startup_db_client():

    settings = get_settings()

    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.include_router(base.base_router)
app.include_router(data.data_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)