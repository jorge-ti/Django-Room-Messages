from django.forms import ModelForm

from .models import Topic as TopicModel
from .models import Room as RoomModel


class TopicForm(ModelForm):
    class Meta():
        model = TopicModel
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta():
        model = RoomModel
        fields = '__all__'
