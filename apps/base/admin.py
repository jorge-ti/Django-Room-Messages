from django.contrib import admin

from .models import Topic as TopicModel
from .models import Room as RoomModel
from .models import Message as MessageModel

admin.site.register(TopicModel)
admin.site.register(RoomModel)
admin.site.register(MessageModel)
