from django.shortcuts import render
import json
# Create your views here.


def index(request):
    return render(request,'index.html')


def room(request,room_name):
    context ={
        'room_name':room_name,
        # 'username':request.user.username,
        'username':request.user.usercostumer.username,
    }
    return render(request,'room.html',context)