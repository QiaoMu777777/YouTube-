from fastapi import APIRouter, BackgroundTasks, Form, Request
from fastapi.templating import Jinja2Templates
from ..core.downloader import downloader
from ..core.utils import get_video_list
from ..config import settings

router = APIRouter()
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "videos": get_video_list()}
    )

@router.post("/download")
async def download(background_tasks: BackgroundTasks, video_url: str = Form(...)):
    import time
    video_id = str(time.time())
    background_tasks.add_task(downloader.download_video, video_url, video_id)
    return {"video_id": video_id}

@router.get("/progress/{video_id}")
async def get_progress(video_id: str):
    return downloader.download_progress.get(video_id, {'status': 'not_found'}) 