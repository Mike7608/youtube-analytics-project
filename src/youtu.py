import json
import os

from googleapiclient.discovery import build


class YouTube:
    __api_key: str = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=cls.__api_key)
        return youtube

    def to_json(self, filename):
        """Сохраняем в файл значения атрибутов экземпляра YouTube"""
        with open(filename, "w") as file:
            json.dump(self.__dict__, file)
