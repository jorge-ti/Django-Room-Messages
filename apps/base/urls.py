from django.urls import path

from .views import Home as UrlHome
from .views import TopicCreate as UrlTopicCreate
from .views import TopicDetail as UrlTopicDetail
from .views import RoomCreate as UrlRoom


urlpatterns = [
    path('', UrlHome.as_view(), name='url_home'),
    path('topic/create/', UrlTopicCreate.as_view(), name='url_topic_create'),
    path('topic/detail/<int>', UrlTopicDetail.as_view(), name='url_topic_detail'),
    path('room/create/', UrlRoom.as_view(), name='url_room_create'),
]