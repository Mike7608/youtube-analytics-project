from src.youtu import YouTube
import isodate
import datetime


class PlayList(YouTube):
    """Класс для плейлиста ютуб-канала"""

    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        playlist = self.get_service().playlists().list(part='snippet', id=playlist_id).execute()

        self.__title = playlist["items"][0]["snippet"]["title"]
        self.__url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @property
    def title(self):
        """
        Наименование плейлиста
        """
        return self.__title

    @property
    def url(self):
        """
        Ссылка на плейлист
        """
        return self.__url

    @property
    def total_duration(self):
        """
        Возвращает суммарное время плейлиста
        """
        video_response = self.get_video_response()

        total_time = 0

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time += duration.total_seconds()
        return datetime.timedelta(seconds=total_time)

    def get_video_response(self):
        """
        Возвращает данные по видеороликам
        """
        # получаем плейлист
        playlist = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                           part='contentDetails', maxResults=50).execute()
        # получает список id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist['items']]
        # получаем данные по видеороликам
        return self.get_service().videos().list(part='contentDetails,statistics',
                                                id=','.join(video_ids)).execute()

    @property
    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео
        """
        video_response = self.get_video_response()
        link = ""
        cl = 0
        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            id_video = video["id"]
            if like_count > cl:
                cl = like_count
                link = id_video
        return f"https://youtu.be/{link}"

