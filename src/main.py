from fastapi import FastAPI
import uvicorn

from routes import base, data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)