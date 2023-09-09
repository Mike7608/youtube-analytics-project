import json
from src.youtu import YouTube


class Channel(YouTube):
    """Класс для ютуб-канала"""

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


