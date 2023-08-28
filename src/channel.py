import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel: dict = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        item = self.channel["items"][0]

        self.__channel_id = item["id"]
        self.title = item["snippet"]["title"]
        self.description = item["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.channel_id
        self.subscriber_count = int(item["statistics"]["subscriberCount"])
        self.video_count = int(item["statistics"]["videoCount"])
        self.view_count = int(item["statistics"]["viewCount"])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """ * """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """ - """
        val1 = self.subscriber_count
        val2 = other.subscriber_count
        return val1 - val2

    def __lt__(self, other):
        """ < """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """ <= """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """ > """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """ > """
        return self.subscriber_count >= other.subscriber_count

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
        youtube = build('youtube', 'v3', developerKey=cls.__api_key)
        return youtube

    def to_json(self, filename):
        """Сохраняем в файл значения атрибутов экземпляра Channel"""
        with open(filename, "w") as file:
            json.dump(self.__dict__, file)
