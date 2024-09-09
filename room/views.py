from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.http import require_http_methods
from todo.models import *
from chat.models import *
# Create your views here.



def show_room_page(request,pk):
    room=Room.objects.get(id=pk)
    
    members=room.members.all()
    todos=Todo.objects.filter(room=room)
    messages=Message.objects.filter(room=room)

    context={
        'members':members,
        'room':room,
        'todos':todos,
        'messages_chat':messages
    }
    return render(request,'room.html',context)





def show_rooms_page(request):
    if request.user.is_authenticated:
       user=request.user 
       search=request.POST.get("search")
       rooms=Room.objects.filter(members=user)
       if search:
           rooms=Room.objects.filter(room_id=search)
           if len(rooms) < 1:
                messages.error(request,"not found this room")
               
                rooms=Room.objects.filter(members=user)
       paginator=Paginator(rooms,1)     
       page_number=request.GET.get("page")
      
       try:
            rooms=paginator.page(page_number)
       except PageNotAnInteger:   
             rooms=paginator.page(1)
       except EmptyPage:   
             rooms=paginator.page(1)

       context={
           'rooms':rooms,
       }
       return render(request,'rooms.html',context)
    return redirect('accounts:show_auth_page')



def check_room_id(request,pk):
    sent_room_id=request.POST.get("roomid")
    room=Room.objects.get(id=pk)
    acutal_room_id=room.room_id
    if acutal_room_id == sent_room_id:
        room.members.add(request.user)
        messages.success(request,"room id entered is correct")
    else:
        messages.error(request,"room id entered is not correct")
    return redirect('room:show_rooms_page')
    
    
    
def change_room_status(request,pk):
    room=Room.objects.get(id=pk)
    room.is_done=not(room.is_done)
    room.save()
    return redirect('room:show_rooms_page')




def logout_room(request,pk):
    room=Room.objects.get(id=pk)
    room.members.remove(request.user)
    return redirect('room:show_rooms_page')



@require_http_methods(['POST'])
def addtodo(request):
    todo = None
    title = request.POST.get('title')
    id = request.POST.get('id')
    room = Room.objects.get(id=id)
    if title :
        todo = Todo(title=title,room=room)
        todo.save()
        todo = model_to_dict(todo)
    return JsonResponse({'todo':todo},safe=False)
    #safe=false لايقوم بالتنفيذ فقط يرسل البيانات كنص
    
    
def tooglestatus(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.is_done=not(todo.is_done)
    todo.save()
    todo = model_to_dict(todo)
    return JsonResponse({'todo':todo},safe=False)
    