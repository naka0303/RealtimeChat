"""chat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat_app'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('make_chatroom/', views.MakeChatroom.as_view(), name='make_chatroom'),
    path('user_list/', views.UserList.as_view(), name='user_list'),
    path('chat/room/<int:pk>', views.ChatRoomList.as_view(), name='chat_room'),
] + static(settings.ICON_URL, document_root=settings.ICON_ROOT)
