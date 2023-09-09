import os
from src.youtu import YouTube


class Video(YouTube):
    """Класс для ютуб видео"""

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


class PLVideo(Video):
    """Класс для ютуб плейлиста"""
    def __init__(self, video_id, id_playlist) -> None:
        super().__init__(video_id)
        self.id_playlist = id_playlist


