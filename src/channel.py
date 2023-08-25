import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel: dict = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        item = self.channel["items"][0]

        self.__channel_id = item["id"]
        self.title = item["snippet"]["title"]
        self.description = item["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.channel_id
        self.subscriber_count = item["statistics"]["subscriberCount"]
        self.video_count = item["statistics"]["videoCount"]
        self.view_count = item["statistics"]["viewCount"]


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


    @property
    def channel_id(self):
        """Возвращает id канала"""
        return self.__channel_id


    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename):
        """Сохраняем в файл значения атрибутов экземпляра Channel"""
        # d = {"channel_id": self.__channel_id, "title": self.title, "description": self.description, "url": self.url,
        #      "subscriber_count": self.subscriber_count, "video_count": self.video_count, "view_count": self.view_count}

        with open(filename, "w") as file:
            json.dump(self.__dict__, file)
