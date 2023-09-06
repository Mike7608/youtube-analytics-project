import os
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб видео"""
    __api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, video_id: str) -> None:

        all_info: dict = self.get_service().videos().list(part="snippet,statistics", id=video_id).execute()

        item = all_info["items"][0]

        self.video_id = item["id"]
        self.video_title = item["snippet"]["title"]
        self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.video_view_count = int(item["statistics"]["viewCount"])
        self.video_like_count = int(item["statistics"]["likeCount"])

    def __str__(self):
        return self.video_title

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=cls.__api_key)
        return youtube


class PLVideo(Video):
    """Класс для ютуб плейлиста"""
    def __init__(self, video_id, id_playlist) -> None:
        super().__init__(video_id)
        self.id_playlist = id_playlist


