from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routers import download
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板
templates = Jinja2Templates(directory="templates")

# 注册路由
app.include_router(download.router)

# 主页路由
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})