from pathlib import Path
from ..config import settings

def get_video_list():
    """获取已下载视频列表"""
    videos = []
    if settings.VIDEOS_DIR.exists():
        for video_file in settings.VIDEOS_DIR.glob('*'):
            if video_file.is_file() and video_file.suffix in ['.mp4', '.webm', '.mkv']:
                videos.append({
                    'filename': video_file.name,
                    'path': f'/static/videos/{video_file.name}',
                    'size': f'{video_file.stat().st_size / (1024*1024):.1f} MB'
                })
    return videos 