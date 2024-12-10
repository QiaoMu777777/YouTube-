from pydantic import BaseModel
from typing import Optional

class VideoProgress(BaseModel):
    status: str
    progress: Optional[str] = None
    speed: Optional[str] = None
    eta: Optional[str] = None
    error: Optional[str] = None

class VideoInfo(BaseModel):
    title: str
    duration: int
    uploader: str
    description: str
    filename: str
    status: str 