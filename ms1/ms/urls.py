
from django.contrib import admin
from django.urls import path
import msapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', msapp.views.home, name='home'),
    path('introduce/', msapp.views.introduce, name='introduce'),
    path('test1/', msapp.views.test1, name='test1'),
    path('test2/', msapp.views.test2, name='test2')
]
