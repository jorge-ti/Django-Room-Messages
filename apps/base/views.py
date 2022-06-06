from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect

from .forms import RoomForm
from .forms import TopicForm
from .forms import MessageForm
from .models import Topic as TopicModel
from .models import Room as RoomModel
from .models import Message as MessageModel


class Home(View):
    template = 'base/home.html'

    def get(self, request, *args, **kwargs):
        topics = TopicModel.objects.all()
        rooms = RoomModel.objects.all()
        messages = MessageModel.objects.order_by('-updated')[:5]
        context = {
            'topics':topics,
            'rooms':rooms,
            'messages':messages
        }
        return render(request, self.template, context)


class TopicCreate(View):
    template = "base/topic_create.html"
    topic = TopicForm()

    def get(self, request, *args, **kwargs):
        context = {'topic':self.topic}
        return render(request, self.template, context)


    def post(self, request, *args, **kwargs):
        form = TopicForm(request.POST)

        if form.is_valid():
            try:
                TopicModel.objects.get(name=request.POST['name'])
                messages.error(request, "Tópico já existente")
                return redirect('url_topic_create')
            except:
                pass

            messages.success(request, "Tópico cadastrado com Sucesso")
            form.save()
            return redirect('url_home')

        return redirect('url_topic_create')


class TopicDetail(View):
    template = 'base/topic_detail.html'

    def get(self, request, *args, **kwargs):
        topic_id = kwargs['int']
        topic = TopicModel.objects.get(id=topic_id)
        rooms = RoomModel.objects.filter(topic=topic_id)
        context = {
            'topic':topic,
            'rooms':rooms
            }
        return render(request, self.template, context)


class RoomCreate(View):
    template = 'base/room_create.html'
    room = RoomForm()

    def get(self, request, *args, **kwargs):
        topics = TopicModel.objects.all()
        context = {
            'room':self.room,
            'topics':topics
        }
        return render(request, self.template, context)


    def post(self, request, *args, **kwargs):
        try:
            host = request.user
            topic = request.POST['topic']
            name = request.POST['name']
            description = request.POST['description']
            topic = TopicModel.objects.get(name=topic)
        except:
            messages.success(request, "Favor verifique os dados")
            return redirect('url_room_create')

        RoomModel.objects.create(
            host = host,
            topic = topic,
            name = name,
            description = description
        )
        messages.success(request, "Sala cadastrada com sucesso")
        return redirect('url_home')


class MessageList(View):
    template = 'base/message_list.html'
    form = MessageForm()

    def get(self, request, *args, **kwargs):
        id_room = kwargs['pk']
        messages = MessageModel.objects.filter(room=id_room)
        context = {
            'messages':messages,
            'form':self.form
        }
        return render(request, self.template, context)


    def post(self, request, *args, **kwargs):
        user = request.user
        id_room = kwargs['pk']
        body = request.POST['body']
        form = MessageForm(request.POST)
        room = RoomModel.objects.get(id=id_room)
        if form.is_valid():
            
            MessageModel.objects.create(
                user = user,
                room = room,
                body = body,
            )
            return redirect('url_message_list', id_room)


class MessageDelete(View):

    def get(self, request, *args, **kwargs):
        id_message = kwargs['pk']
        MessageModel.objects.filter(id=id_message).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

