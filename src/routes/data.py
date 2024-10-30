from fastapi import FastAPI, APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import aiofiles
import logging

logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    
    is_valid, result_signal = DataController().validate_uploaded_file(file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "result": "error",
                "signal": result_signal,
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)

    file_path = os.path.join(
        project_dir_path,
        file.filename
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "result": "error",
                "signal": result_signal,
            }
        )

    return JSONResponse(
        content={
            "result": "success",
            "signal": ResponseSignal.File_UPLOAD_SUCCESS.value,
        }
    )