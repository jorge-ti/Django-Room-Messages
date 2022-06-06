from django.urls import path

from .views import Home as UrlHome
from .views import TopicCreate as UrlTopicCreate
from .views import TopicDetail as UrlTopicDetail
from .views import RoomCreate as UrlRoomCreate
from .views import MessageList as UrlMessageList
from .views import MessageDelete as UrlMessageDelete


urlpatterns = [
    path('', UrlHome.as_view(), name='url_home'),
    path('topic/create/', UrlTopicCreate.as_view(), name='url_topic_create'),
    path('topic/detail/<int>', UrlTopicDetail.as_view(), name='url_topic_detail'),
    path('room/create/', UrlRoomCreate.as_view(), name='url_room_create'),
    path('room/messages/', UrlMessageList.as_view(), name='url_message_create'),
    path('room/messages/<int:pk>', UrlMessageList.as_view(), name='url_message_list'),
    path('room/messages/delete/<int:pk>', UrlMessageDelete.as_view(), name='url_message_delete'),
]