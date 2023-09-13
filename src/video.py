from src.youtu import YouTube


class Video(YouTube):
    """Класс для ютуб видео"""

    def __init__(self, video_id: str) -> None:
        try:
            all_info: dict = self.get_service().videos().list(part="snippet,statistics", id=video_id).execute()
            item = all_info["items"][0]
            self.id = item["id"]
            self.title = item["snippet"]["title"]
            self.url = f"https://www.youtube.com/watch?v={self.id}"
            self.view_count = int(item["statistics"]["viewCount"])
            self.like_count = int(item["statistics"]["likeCount"])
        except:
            self.id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс для ютуб плейлиста"""

    def __init__(self, video_id, id_playlist) -> None:
        super().__init__(video_id)
        self.id_playlist = id_playlist
