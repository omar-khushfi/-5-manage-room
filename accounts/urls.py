
from django.contrib import admin
from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
   path('show_auth_page/',views.show_auth_page,name="show_auth_page"),
   path('show_profile_page/',views.show_profile_page,name="show_profile_page"),
   path('update_profile/',views.update_profile,name="update_profile"),
   path('show_profile_page/',views.show_profile_page,name="show_profile_page"),
   path('login/',views.login_view,name="login_view"),
   path('logout/',views.logout_view,name="logout_view"),
   path('signup/',views.signup_view,name="signup_view")
]
