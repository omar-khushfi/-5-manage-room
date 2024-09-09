
from django.contrib import admin
from django.urls import path
from . import views
app_name='room'
urlpatterns = [
    path('show_room_page/<int:pk>',views.show_room_page,name='show_room_page'),
    path('check_room_id/<int:pk>',views.check_room_id,name='check_room_id'),
    path('change_room_status/<int:pk>',views.change_room_status,name='change_room_status'),
    path('logout_room/<int:pk>',views.logout_room,name='logout_room'),
    path('',views.show_rooms_page,name='show_rooms_page'),
    path('addtodo/',views.addtodo,name='addtodo'),
    path('togglestatus/<int:pk>',views.tooglestatus,name='tooglestatus')
    
]
