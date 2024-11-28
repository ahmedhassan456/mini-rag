from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATION_SUCCESS = "File validation successfully"
    File_TYPE_NOT_SUPPORTED = "File type not supported"
    File_SIZE_EXCEEDED = "File size exceeded"
    File_UPLOAD_SUCCESS = "File uploaded successfully"
    File_UPLOAD_FAILED = "File upload failed"
    PROCESSING_FAILED = "Processing failed"
    PROCESSING_SUCCESS = "Processing success"
    NO_FILES_ERROR = "Not found files"
    FILE_ID_ERROR = "No file found with this id"