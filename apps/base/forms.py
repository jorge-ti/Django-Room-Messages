from django.forms import ModelForm

from .models import Topic as TopicModel
from .models import Room as RoomModel
from .models import Message as MessageModel


class TopicForm(ModelForm):
    class Meta():
        model = TopicModel
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta():
        model = RoomModel
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta():
        model = MessageModel
        fields = ['body']
