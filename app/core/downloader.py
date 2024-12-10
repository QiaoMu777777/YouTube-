from typing import Dict, Optional
import yt_dlp
from ..config import settings

class VideoDownloader:
    def __init__(self):
        self.download_progress: Dict[str, dict] = {}
        
    def progress_hook(self, video_id: str):
        def hook(d):
            if d['status'] == 'downloading':
                self.download_progress[video_id].update({
                    'status': 'downloading',
                    'progress': d.get('_percent_str', '0%'),
                    'speed': d.get('_speed_str', 'N/A'),
                    'eta': d.get('_eta_str', 'N/A')
                })
            elif d['status'] == 'finished':
                self.download_progress[video_id]['status'] = 'finished'
        return hook
    
    async def download_video(self, video_url: str, video_id: str) -> Optional[Dict]:
        self.download_progress[video_id] = {'status': 'starting'}
        
        ydl_opts = {
            'format': settings.DEFAULT_FORMAT,
            'outtmpl': str(settings.VIDEOS_DIR / '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook(video_id)],
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                file_path = str(settings.VIDEOS_DIR / f"{info['title']}.{info['ext']}")
                self.download_progress[video_id].update({
                    'title': info.get('title', ''),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', ''),
                    'description': info.get('description', ''),
                    'filename': f"{info['title']}.{info['ext']}",
                    'file_path': file_path,
                    'status': 'finished'
                })
                return self.download_progress[video_id]
        except Exception as e:
            self.download_progress[video_id].update({
                'status': 'error',
                'error': str(e)
            })
            return None

downloader = VideoDownloader() 