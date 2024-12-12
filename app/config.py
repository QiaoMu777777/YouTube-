from pathlib import Path
import os

# 基础配置
class Settings:
    PROJECT_NAME: str = "乔木YouTube视频下载"
    VERSION: str = "1.0.0"
    API_PREFIX: str = ""
    
    # 路径配置
    BASE_DIR: Path = Path(__file__).parent.parent
    STATIC_DIR: Path = BASE_DIR / "static"
    VIDEOS_DIR: Path = Path("/tmp/videos") if os.environ.get("RAILWAY_STATIC_URL") else BASE_DIR / "static/videos"
    TEMPLATES_DIR: Path = BASE_DIR / "templates"
    
    # 下载配置
    DEFAULT_FORMAT: str = "best"
    MAX_DOWNLOAD_CONCURRENCY: int = 3
    
    # 确保必要的目录存在
    def create_directories(self):
        self.VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

# 修改下载路径配置
DOWNLOAD_PATH = '/home/你的用户名/YouTube下载器/downloads'  # PythonAnywhere 的路径

settings = Settings()
settings.create_directories() 